# 토큰 발급
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.testing.pickleable import User

from auth import db, get_user

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


# token 데이터를 해것하는 함수
def decode_token(token):
    return get_user(db, token)


# 인증된 유저 정보 return (현재 토큰을 사용하고 있는 유저 정보 리턴)
def get_current_user(token: str = Depends(oauth2_schema)):
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


import schemas


# 인증이 활성화 되어 있는가 (활성화 되어 있으면 pass, 안되어 있으면 400)
def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return current_user
