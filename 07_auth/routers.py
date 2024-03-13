from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import db
import schemas

router = APIRouter()


@router.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = db.get(form_data.username)
    user = schemas.CreateUser(**user_dict)
    if user.hashed_password == form_data.password:
        return {"access_token": "123123123", "refresh_token": "13123123123"}
