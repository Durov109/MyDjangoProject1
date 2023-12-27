# Используем официальный образ Python
FROM python:alpine

# Создаем директорию приложения
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Порт
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver"]