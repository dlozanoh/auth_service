# 🔐 Authentication Service with JWT, PostgreSQL, and Redis

A secure, containerized authentication microservice built with **FastAPI**, using **JWT** for stateless authentication, **PostgreSQL** for persistent user storage, and **Redis** for token blacklisting (logout).

---

## 🚀 Features

- ✅ Login with username/password
- 🔐 JWT token issuance on successful login
- 🔁 Token blacklist on logout (Redis)
- 🔒 Protected route with token validation
- 🧂 SHA-256 password hashing
- 🐳 Fully Dockerized environment (API + PostgreSQL + Redis)
- ⚙️ Auto-initialized database with test user

---

## 📦 Tech Stack

- **FastAPI** (Python)
- **PostgreSQL**
- **Redis 7**
- **JWT (HS256)**
- **Docker + Docker Compose**

---

## 📁 Project Structure

```text
📦 auth_service/
 ┣ 📂 app/                            → Application logic
 ┃ ┣ 📄 main.py                      → FastAPI app & route definitions
 ┃ ┣ 📄 auth.py                      → JWT creation and decoding
 ┃ ┣ 📄 database.py                  → MySQL DB connection & user verification
 ┃ ┣ 📄 redis_blacklist.py           → Redis-based token blacklisting
 ┃ ┗ 📄 models.py                    → Pydantic schemas
 ┣ 📄 init.sql                        → SQL script to initialize DB & default user
 ┣ 📄 .env                            → Environment variables for config
 ┣ 📄 requirements.txt                → Python package dependencies
 ┣ 📄 Dockerfile                      → Docker image build for the API
 ┣ 📄 docker-compose.yml              → Service orchestration: API + DB + Redis
 ┗ 📄 README.md                       → Project documentation
```


## ▶️ Run it

```bash
# Start the service
docker-compose up --build

# Access the docs
http://localhost:8000/docs

# Using Makefile
make up          # Start the app
make test        # Run unit tests
make format      # Format code with Black
make redis-cli   # Access Redis CLI


---

## 🔧 Environment Variables (`.env`)

```env

SECRET_KEY=your_super_secret_key
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=authdb
REDIS_HOST=redis

| Method | Endpoint     | Description                         |
| ------ | ---------    | ----------------------------------- |
| POST   | `/signup`    | Register and create user            |    
| POST   | `/login`     | Authenticates and returns JWT       |
| POST   | `/logout`    | Invalidates current JWT token       |
| GET    | `/me`        | Returns user info if token is valid |
