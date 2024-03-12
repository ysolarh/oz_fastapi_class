from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import dependencies
import crud
import schemas

router = APIRouter()

@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    item = crud.get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# items => skip, limit
@router.get("/")
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    items = crud.get_items(db, skip, limit)
    return items

@router.post("/")
def create_item(item: schemas.ItemCreate, owner_id: int, db: Session = Depends(dependencies.get_db)):
    item = crud.create_item(db, item, owner_id)
    return item

@router.put("/{item_id}")
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session = Depends(dependencies.get_db)):
    item = crud.update_item(db, item_id, item_update)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    is_success = crud.delete_item(db, item_id)

    if not is_success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"msg": "Success delete item"}
