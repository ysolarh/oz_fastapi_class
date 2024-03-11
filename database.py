from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 동기용 데이터 베이스 설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:akdls@localhost/oz_fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# fastapi 특징
# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

# 비동기용 데이터 베이스 설정 -> aiomysql
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://root:akdls@localhost/oz_fastapi'
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()
