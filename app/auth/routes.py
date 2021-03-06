from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.auth import schemas, helpers


auth = APIRouter()
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@auth.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = helpers.authenticate_user(helpers.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = helpers.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(helpers.get_current_active_user)):
    return current_user

@auth.get("/users/me/items/")
async def read_own_items(current_user: schemas.User = Depends(helpers.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
