from fastapi import FastAPI
from items import router as items_router
from users import router as users_router
from 02_sync-async.sync_async_test import router as sync_async_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)
app.include_router(sync_async_router)

# @app.get('/')
# def index():
#     return "Hello World!"
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, query: str = None):
#     data = {"item_id": item_id, "query": query}
#     return data
# # http://127.0.0.1:5000/items/1?query=data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="debug", reload=True)
