import mysql.connector
import os
import hashlib

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "db"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "password"),
    database=os.getenv("MYSQL_DB", "authdb")
)
cursor = conn.cursor(dictionary=True)

def verify_user(username: str, password: str):
    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, hashed_pwd))
    return cursor.fetchone() is not None
