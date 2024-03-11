from fastapi import APIRouter
from fastapi import HTTPException

from models import Movie
from movie_db import movie_db

router = APIRouter()


# [GET] - 모든 영화 목록 반환
@router.get("/")
def get_movies():
    # ORM or SQL Query
    return movie_db


# [POST] - 새로운 영화 생성
@router.post("/")
def create_movie(request: Movie):
    movie = request.model_dump()
    movie_db.append(movie)
    return {'id': len(movie_db)}


# [PUT]/{id} - 특정 영화 정보 업데이트
@router.put("/{id}")
def update_movie(id: int, request: Movie):
    movie = request.model_dump()
    movie_db[id] = movie
    return movie_db


# [DELETE]/{id} - 특정 영화 삭제
@router.delete("/{id}")
def delete_movie(id: int):
    if 0 < id <= len(movie_db):
        del movie_db[id]
        return None
    return HTTPException(404, "Movie is not found")
