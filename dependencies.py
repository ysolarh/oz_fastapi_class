from fastapi import HTTPException

from database import SessionLocal


# 동기용 의존성
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# 비동기용 의존성
from database import AsyncSessionLocal


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
        

def response(data):
    if data is None:
        raise HTTPException(status_code=404, detail=f"{data} Not Found")
    return data
