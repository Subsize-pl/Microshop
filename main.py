from fastapi import FastAPI
from routers import products_router
from auth import auth_router

app = FastAPI()
app.include_router(router=products_router)
app.include_router(router=auth_router)
