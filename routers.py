from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import dependencies

import schemas

router = APIRouter()


@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    db_user = crud.create_user(db, user)
    return db_user

