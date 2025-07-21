# FSTR API

Проект API сервиса ФСТР — загрузка данных о перевалах.

## 🔗 Деплой

- Swagger: https://fstr-api.onrender.com/docs  
- ReDoc: https://fstr-api.onrender.com/redoc

## 🚀 Возможности

- `POST /submitData` — создать перевал
- `GET /submitData/{id}` — получить по ID
- `PATCH /submitData/{id}` — обновить, если status == "new"
- `GET /submitData/?user__email=...` — все перевалы пользователя

## 🧪 Запуск проекта

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## ⚙️ Переменные окружения

Создайте `.env` на основе `.env.example`:

```env
FSTR_DB_HOST=localhost
FSTR_DB_PORT=5432
FSTR_DB_NAME=fstr_db
FSTR_DB_LOGIN=postgres
FSTR_DB_PASS=your_password
```

## 🧪 Тесты

```bash
pytest
```

## 🛠️ Стек

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Swagger / OpenAPI

## 👨‍💻 Автор

[Ваше имя]  
[Контакты / Telegram / GitHub]
