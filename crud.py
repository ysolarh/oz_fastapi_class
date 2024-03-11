from sqlalchemy.orm import Session
import bcrypt

from models import User
from schemas import UserCreate


# create user
def create_user(db: Session, db_user: UserCreate):
    hashed_password = bcrypt.hashpw(db_user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(email='exampledf@test.com', hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user
