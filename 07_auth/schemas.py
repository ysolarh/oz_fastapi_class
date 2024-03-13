# data validation -> pydantic
from pydantic import BaseModel


# REST API response
class User(BaseModel):
    email: str
    username: str | None = None


# DB에 데이터 저장할 때
class CreateUser(User):
    hashed_password: str
