from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException
from app.database import verify_user
from app.redis_blacklist import blacklist_token, is_blacklisted
from app.models import Token
import os

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def login_user(username: str, password: str) -> Token:
    if not verify_user(username, password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": username})
    return Token(access_token=access_token, token_type="bearer")

def logout_token(token: str):
    blacklist_token(token)

def get_current_user(token: str):
    if is_blacklisted(token):
        raise HTTPException(status_code=401, detail="Token blacklisted")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
