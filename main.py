from fastapi import FastAPI
from auth_routes import auth_router
from oder_routes import order_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
