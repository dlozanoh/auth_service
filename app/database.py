import psycopg2
import os
import hashlib

conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "db"),
    port=int(os.getenv("POSTGRES_PORT", 5432)),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "password"),
    dbname=os.getenv("POSTGRES_DB", "authdb")
)
cursor = conn.cursor()

def verify_user(username: str, password: str):
    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute(
        "SELECT id FROM users WHERE username=%s AND password=%s",
        (username, hashed_pwd)
    )
    return cursor.fetchone() is not None
