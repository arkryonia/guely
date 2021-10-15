
from fastapi import Depends, FastAPI, HTTPException, status

from app.auth.routes import auth

app = FastAPI()

app.include_router(auth, tags=["Users"])




