from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str

def fake_decode_token(token):
    return User(username=token+"fakedecoded")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return User

@app.get("/user/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user