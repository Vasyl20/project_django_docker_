# Базовий образ
FROM python:3.12

# Встановлення робочої директорії
WORKDIR /myproject

# Копіювання requirements.txt
COPY requirements.txt /myproject

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django django-prometheus

# Копіювання проекту
COPY . /myproject

# Команда для запуску
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]