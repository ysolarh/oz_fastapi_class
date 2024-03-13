import schemas


db = {
    "admin": {
        "email": "admin@example.com",
        "username": "admin",
        "hashed_password": "secret"
    }
}


def get_user(db, username: str):
    if username in db:
        return schemas.CreateUser(**db[username])
