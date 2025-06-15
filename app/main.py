from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app import auth, database, redis_blacklist

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not database.verify_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    redis_blacklist.add_to_blacklist(token)
    return {"msg": "Token blacklisted"}

@app.get("/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    if redis_blacklist.is_blacklisted(token):
        raise HTTPException(status_code=401, detail="Token is blacklisted")
    payload = auth.decode_token(token)
    return {"username": payload.get("sub")}
