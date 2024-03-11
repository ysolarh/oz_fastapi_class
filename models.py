# User, Item
# DB Connection
from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    # items = relationship('Item', back_populates='owner')

    # CREATE TABLE users(
    #   id INT PRIMARY KEY AUTO_INCREMENT,
    #   email VARCHAR(255),
    #   hashed_password VARCHAR(255)
    # )


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    # owner = relationship('User', back_populates='items')

# User와 Item의 관계
