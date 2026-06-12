# 📗 Ansible Manager

Web-based platform for managing and executing Ansible automation tasks through a modern Django interface.

## Overview

Ansible Automation is a self-hosted platform that combines:

* Django web interface
* Ansible automation engine
* Docker-based deployment

The platform allows administrators to manage infrastructure automation, execute playbooks, schedule tasks, and maintain server inventories from a centralized web dashboard.

![Project demo](https://github.com/alexanderlucky/ansible_manager/blob/main/demo.png?raw=true)
---

## Quick Start 🚀

### Clone Repository

```bash
git clone https://github.com/alexanderlucky/ansible_automation.git
```
```bash
cd ansible_automation
```

### Start Containers

```bash
docker compose build --no-cache
```
```bash
docker compose up -d
```

### Open ansible manager
[http://localhost:8000](http://localhost:8000)


### Ollama setup (optional)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

```bash
ollama run qwen2.5
```

---

## ⭐ Features

### Infrastructure Automation

* Execute Ansible playbooks from the web interface
* Manage inventories and hosts
* Store automation templates
* Centralized execution history

### Task Scheduling

* Schedule recurring automation jobs
* Run maintenance workflows automatically
* Track execution status

### Server Management

* Linux server automation
* SSH-based remote execution
* Credential management
* Inventory grouping

### Monitoring & Logging

* Execution logs
* Task history
* Error tracking
* Audit trail

### Containerized Deployment

* Docker Compose deployment
* Easy environment management

---


## 🛠 Tech Stack

### Backend

* Python 3.12+
* Django 5+
* Ansible

### Infrastructure

* Docker
* Docker Compose

---

## 📚 Project Structure

```text
ansible_automation/
│
├── ansible/
│   ├── manage.py
│   ├── requirements.txt
│   ├── playbooks/
│   └── catalog/
│
├── convert.sh
├── docker-compose.yml
├── README.md
```

---


## 🧩 Services

| Service    | Port |
| ---------- | ---- |
| Django     | 8000 |


---

## 🚪 Access

### Django Application

```text
http://localhost:8000
```

---

## ⛏ Development

Rebuild containers:

```bash
docker compose down
docker compose up --build -d
```

View logs:

```bash
docker compose logs -f django
```

Open shell:

```bash
docker exec -it ansible_django bash
```

---

## 🗺 Roadmap

* [ ] Inventory management UI
* [ ] REST API
* [ ] Multi-user support
* [ ] RBAC permissions

---

## 👨‍💼 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## License

MIT License

---

## Author

Alexander Lucky

GitHub:
https://github.com/alexanderlucky
