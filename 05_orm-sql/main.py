from fastapi import FastAPI
from routers.users import router as user_routers
from routers.items import router as item_routers

app = FastAPI()

app.include_router(user_routers, prefix='/api/v1/users', tags=['User'])
app.include_router(item_routers, prefix='/api/v1/items', tags=['Item'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
