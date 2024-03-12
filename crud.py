from sqlalchemy.orm import Session
import bcrypt

from models import User
from schemas import UserCreate, UserUpdate


# create user
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


# user의 id값을 기반으로 데이터를 찾는다.
#
# def get_user_id(db: Session, payload: User): - 비추
def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# user의 eamil값을 기반으로 데이터를 찾는다.
def get_user_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


# 전체 유저를 불러오기 (페이지네이션)
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    user_data = user_update.dict()
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
