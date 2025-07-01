import psycopg2
import os
import hashlib

# conn = psycopg2.connect(
#     host=os.getenv("POSTGRES_HOST", "db"),
#     port=int(os.getenv("POSTGRES_PORT", 5432)),
#     user=os.getenv("POSTGRES_USER", "postgres"),
#     password=os.getenv("POSTGRES_PASSWORD", "password"),
#     dbname=os.getenv("POSTGRES_DB", "authdb")
# )
# cursor = conn.cursor()


DB_HOST = os.getenv("POSTGRES_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_NAME = os.getenv("POSTGRES_DB", "authdb")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    
def verify_user(username: str, password: str) -> bool:
    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username=%s AND password=%s",
        (username, hashed_pwd)
    )
    return cursor.fetchone() is not None

def user_exists(username: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
    exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()
    return exists

def create_user(username: str, password: str) -> None:
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT (username) DO NOTHING",
        (username, hashed)
    )
    conn.commit()
    cur.close()
    conn.close()