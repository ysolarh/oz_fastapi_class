from sqlalchemy.sql import text
from sqlalchemy.orm import Session
import bcrypt

from models import User, Item
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate


# ORM -> SQL 방식 활용
# create user
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    # db_user = User(email=user.email, hashed_password=hashed_password)
    # db.add(db_user)

    sql = text("INSERT INTO users(email, hashed_password) VALUES(:email, :hashed_password)")
    db.execute(sql, {"email": user.email, "hashed_password": hashed_password})
    db.commit()

    sql = text("SELECT LAST_INSERT_ID()")  # 가장 마지막에 생성된 유저 ID 리턴
    last_id_result = db.execute(sql)
    last_id = last_id_result.scalar()  # 파이썬이 이해할수 있게 바꿔줌

    sql = text("SELECT * FROM users WHERE id = :last_id")
    result = db.execute(sql, {"last_id": last_id}).fetchone()

    print('result1:', result)
    print('result2:', type(result))
    print('result3:', result._asdict())

    # return db_user
    return result._asdict()


# user의 id값을 기반으로 데이터를 찾는다.
#
# def get_user_id(db: Session, payload: User): - 비추
def get_user_id(db: Session, user_id: int):
    # return db.query(User).filter(User.id == user_id).first()
    sql = text("SELECT * FROM users WHERE id = :user_id")
    result = db.execute(sql, {"user_id": user_id}).fetchone()  # object -> row
    return result._asdict()  # dict


# user의 eamil값을 기반으로 데이터를 찾는다.
def get_user_email(db: Session, user_email: str):
    # return db.query(User).filter(User.email == user_email).first()
    sql = text("SELECT * FROM users WHERE email = :user_email")
    result = db.execute(sql, {"user_email": user_email}).fetchone()
    return result._asdict()


# 전체 유저를 불러오기 (페이지네이션)
def get_users(db: Session, skip: int = 0, limit: int = 10):
    # return db.query(User).offset(skip).limit(limit).all()
    sql = text("SELECT * FROM users LIMIT :limit OFFSET :skip")
    results = db.execute(sql, {"limit": limit, "skip": skip}).fetchall()  # [row, row, row, ...]
    users = [row._asdict() for row in results]
    return users


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    user_data = user_update.dict()
    data = ", ".join([f"{key} = :{key}" for key in user_data])
    print('data:', data)

    sql = text(f"UPDATE users SET {data} WHERE id = :user_id")
    print('sql:', sql)

    user_data["user_id"] = user_id
    db.execute(sql, user_data)
    db.commit()
    return get_user_id(db, user_id)

    # db_user = db.query(User).filter(User.id == user_id).first()
    # if not db_user:
    #     return None
    # user_data = user_update.dict()
    # for key, value in user_data.items():
    #     setattr(db_user, key, value)
    # db.commit()
    # db.refresh(db_user)
    # return db_user


def delete_user(db: Session, user_id: int):
    sql = text("DELETE FROM users WHERE id = :user_id")  # ON DELETE CASCADE
    db.execute(sql, {'user_id': user_id})
    db.commit()
    return {'id': user_id}

    # db_user = db.query(User).filter(User.id == user_id).first()
    # if not db_user:
    #     return None
    # db.delete(db_user)
    # db.commit()
    # return db_user


# Item -> CRUD
# 하나의 아이템 데이터 조회
def get_item(db: Session, item_id: int):
    # return db.query(Item).filter(Item.id == item_id).first()
    sql = text("SELECT * FROM items WHERE id = :item_id")
    result = db.execute(sql, {'item_id': item_id}).fetchone()
    return result._asdict()

    # 장고에서 get() => 2개 이상 나오면 오류 발생. get_object, get_object_or_404


# 전체 아이템 데이터 조회 (limit: 20 ~ 100)
# pagination -> 1 ~ 10개 데이터. 11 ~ 20, 21 ~ 31
#
def get_items(db: Session, skip: int = 0, limit: int = 10):
    # return db.query(Item).offset(skip).limit(limit).all()
    # return db.query(Item).order_by(Item.id.desc()).offset(skip).limit(limit).all()

    sql = text("SELECT * FROM items ORDER BY id DESC LIMIT :limit OFFSET :skip")
    results = db.execute(sql, {"limit": limit, "skip": skip}).fetchall()  # OBJECTS -> [row, row, row]
    return [item._asdict() for item in results]


# 하나의 데이터 생성
def create_item(db: Session, item: ItemCreate, owner_id: int):
    # db_item = Item(**item.dict(), owner_id=owner_id)
    # db.add(db_item)
    # db.commit()
    # db.refresh(db_item)
    # return db_item

    item_data = item.dict()
    item_data['owner_id'] = owner_id
    sql = text("INSERT INTO items(title, description, owner_id) VALUES (:title, :description, :owner_id)")
    db.execute(sql, item_data)
    db.commit()

    sql = text("SELECT LAST_INSERT_ID()")
    result = db.execute(sql)
    last_id = result.scalar()

    sql = text("SELECT * FROM items WHERE id = :last_id")
    result = db.execute(sql, {'last_id': last_id}).fetchone()
    return result._asdict()


# 하나의 데이터 업데이트 {item_id}
def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    # db_item = db.query(Item).filter(Item.id == item_id).first()
    # if not db_item:
    #     return None
    #
    # for key, value in item_update.dict().items():
    #     setattr(db_item, key, value)
    #
    # db.commit()
    # db.refresh(db_item)
    # return db_item

    item_data = item_update.dict()
    data = ", ".join([f"{key} = :{key}" for key in item_data])  # {key:value, key:value}

    item_data['item_id'] = item_id
    sql = text(f"UPDATE items SET {data} WHERE id = :item_id")
    db.execute(sql, item_data)
    db.commit()
    return get_item(db, item_id)


# 하나의 데이터 삭제 {item_id}
def delete_item(db: Session, item_id: int):
    # db_item = db.query(Item).filter(Item.id == item_id).first()
    # if not db_item:
    #     return None
    # db.delete(db_item)
    # db.commit()
    # return True

    sql = text("DELETE FROM items WHERE id = :item_id")
    db.execute(sql, {'item_id': item_id})
    db.commit()
    return {'msg': 'Success delete item', 'id': item_id}
