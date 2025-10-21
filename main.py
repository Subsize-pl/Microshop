from fastapi.responses import ORJSONResponse
import uvicorn
from fastapi import FastAPI
from routers import products_router
from auth import auth_router

app = FastAPI(
    default_response_class=ORJSONResponse,
)
app.include_router(router=products_router)
app.include_router(router=auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=False)
