# 🔐 Authentication Microservice (Python + FastAPI + JWT)

A lightweight authentication microservice handling user registration and login with JWT.

## 🚀 Features
- FastAPI-based REST API
- JWT-based login flow
- User registration endpoint
- Ready to deploy with Docker

## 🛠️ Stack
- FastAPI
- JWT (python-jose)
- Docker

## ▶️ Run it

```bash
# Start the service
docker-compose up --build

# Access the docs
http://localhost:8000/docs

## Project structure

auth_service/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── auth.py                # Auth functions (login, logout, token)
│   ├── database.py            # MySQL connection
│   ├── redis_blacklist.py     # Funciones de blacklist con Redis
│   └── models.py              # Modelos Pydantic
│
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación del proyecto
└── .env                       # Variables de entorno (no subir a GitHub)
