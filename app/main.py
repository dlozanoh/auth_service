from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="Auth Service")


app.include_router(auth.router, prefix="/auth", tags=["auth"])
