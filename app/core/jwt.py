import redis
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Conectar a Redis (asumiendo localhost, puerto 6379)
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def add_token_to_blacklist(token: str, expires_in_seconds: int):
    """Agrega token a Redis con expiración"""
    redis_client.setex(token, expires_in_seconds, "blacklisted")

def is_token_blacklisted(token: str) -> bool:
    """Verifica si el token está en blacklist"""
    return redis_client.get(token) == "blacklisted"

def decode_token(token: str):
    """Decodifica y valida token, además verifica blacklist"""
    if is_token_blacklisted(token):
        raise JWTError("Token is blacklisted")
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
