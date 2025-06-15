# 🔐 Authentication Service with JWT, MySQL, and Redis

A secure, containerized authentication microservice built with **FastAPI**, using **JWT** for stateless authentication, **MySQL** for persistent user storage, and **Redis** for token blacklisting (logout).

---

## 🚀 Features

- ✅ Login with username/password
- 🔐 JWT token issuance on successful login
- 🔁 Token blacklist on logout (Redis)
- 🔒 Protected route with token validation
- 🧂 SHA-256 password hashing
- 🐳 Fully Dockerized environment (API + MySQL + Redis)
- ⚙️ Auto-initialized database with test user

---

## 📦 Tech Stack

- **FastAPI** (Python)
- **MySQL 8**
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


---

## 🔧 Environment Variables (`.env`)

```env
SECRET_KEY=your_super_secret_key
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DB=authdb
REDIS_HOST=redis

