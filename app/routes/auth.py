from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserLogin
from app.core.jwt import create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    # Simulación de guardado y validación
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin):
    # Aquí deberías validar contra base de datos real
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
