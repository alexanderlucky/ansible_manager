import subprocess
import threading
import queue
import os
import pexpect
from django.conf import settings

output_queue = queue.Queue()
task_queue = queue.Queue()
current_process = None
current_name = None
worker_thread = None
lock = threading.Lock()

import subprocess
import threading
import queue
import os
import pexpect
from django.conf import settings

def _run_playbook(name):
    playbook_dir = os.path.join(settings.BASE_DIR, 'playbooks')
    yml_path = os.path.join(playbook_dir, f'{name}.yml')
    ini_path = os.path.join(playbook_dir, f'{name}.ini')

    if not os.path.exists(yml_path) or not os.path.exists(ini_path):
        output_queue.put(f"[ОШИБКА] Файлы плейбука {name} не найдены")
        return

    cmd = f'ansible-playbook -i {ini_path} {yml_path} -v'
    my_env = os.environ.copy()
    my_env.update({
        'ANSIBLE_CONFIG': os.path.join(playbook_dir, 'ansible.cfg'),
        'PYTHONUNBUFFERED': '1',
        'ANSIBLE_FORCE_COLOR': '0',
        'ANSIBLE_NOCOLOR': '1',
        'ANSIBLE_STDOUT_CALLBACK': 'default',
    })

    # 1. Сигнал о старте
    output_queue.put(f"--- Запуск плейбука '{name}' ---")

    try:
        # 2. Запуск и ожидание полного завершения
        child = pexpect.spawn(
            '/bin/bash', ['-c', f'{cmd} 2>&1'],
            env=my_env,
            encoding='utf-8',
            timeout=None
        )
        global current_process, current_name
        with lock:
            current_process = child
            current_name = name

        child.expect(pexpect.EOF)          # ждём конца
        output = child.before              # весь вывод разом

        # 3. Вывод – одним куском
        if output:
            output_queue.put(output.strip())

        # 4. Итоговое сообщение
        if child.exitstatus == 0:
            output_queue.put(f"--- Плейбук '{name}' успешно завершён ---")
        else:
            output_queue.put(f"--- Ошибка выполнения плейбука '{name}' (код {child.exitstatus}) ---")

    except Exception as e:
        output_queue.put(f"[ОШИБКА] {str(e)}")
    finally:
        with lock:
            current_process = None
            current_name = None

def _worker():
    while True:
        name = task_queue.get()
        _run_playbook(name)
        task_queue.task_done()

def start_worker():
    global worker_thread
    if worker_thread is None or not worker_thread.is_alive():
        worker_thread = threading.Thread(target=_worker, daemon=True)
        worker_thread.start()

def submit_task(name):
    task_queue.put(name)
    output_queue.put(f"[ОЧЕРЕДЬ] Плейбук '{name}' добавлен в очередь")

def is_running():
    with lock:
        return current_process is not None and current_process.isalive()