from fastapi import APIRouter, HTTPException, Depends, Header
from app.schemas.user import UserCreate, UserLogin
from app.core.jwt import create_access_token, decode_token, add_token_to_blacklist
from jose import JWTError

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

@router.post("/logout")
def logout(authorization: str = Header(...)):
    """
    Endpoint para logout que agrega el token al blacklist.
    Se espera header Authorization: Bearer <token>
    """
    try:
        token = authorization.split(" ")[1]
        payload = decode_token(token)
        # Calcular segundos restantes del token
        exp_timestamp = payload.get("exp")
        now_timestamp = datetime.utcnow().timestamp()
        expires_in = int(exp_timestamp - now_timestamp)
        if expires_in > 0:
            add_token_to_blacklist(token, expires_in)
        return {"message": "Successfully logged out"}
    except (IndexError, JWTError):
        raise HTTPException(status_code=401, detail="Invalid token")
