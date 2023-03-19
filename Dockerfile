# Устанавливаем базовый образ
FROM python:3.9-slim

# Создаем рабочую директорию для приложения
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

RUN python -m pip install --upgrade pip

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Запускаем приложение
CMD [ "python", "bot.py" ]