# Используем официальный образ Python
FROM python:3.11

# Создаем директорию приложения
WORKDIR /app

# Копируем файл зависимостей (точка означает что файл находится там же где и докерфайл)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

COPY . .

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]