FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ansible \
    openssh-client \
    sshpass \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]