from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer, HTTPAuthorizationCredentials
from app.auth import login_user, logout_token, get_current_user
from app.models import Token
from app.redis_blacklist import is_blacklisted

app = FastAPI()
security = HTTPBearer()

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user(form_data.username, form_data.password)

@app.post("/logout")
def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if is_blacklisted(token):
        raise HTTPException(status_code=400, detail="Token already blacklisted")
    logout_token(token)
    return {"msg": "Logged out"}

@app.get("/me")
def me(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return get_current_user(credentials.credentials)
