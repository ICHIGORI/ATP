# Базовый образ с установленным Python
FROM python:3.14.0-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем в контейнер все файлы вашего проекта
COPY . .

# Команда для запуска по умолчанию (запуск всех тестов)
CMD ["pytest", "-v"]