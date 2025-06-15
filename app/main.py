from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app import auth, database, redis_blacklist

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not database.verify_user(form_data.username, form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials")
    token = auth.create_access_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


