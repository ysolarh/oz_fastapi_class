from fastapi import FastAPI
from routers import router as movie_router

app = FastAPI()

app.include_router(movie_router, prefix="/api/v1/movies", tags=["movies"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", log_level="debug", reload=True)
