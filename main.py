from fastapi import FastAPI
from routers import router as user_routers

app = FastAPI()

app.include_router(user_routers, prefix='/api/v1/users', tags=['User'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
