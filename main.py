from fastapi import FastAPI
from routers import products_router
import asyncio


app = FastAPI()
app.include_router(router=products_router)


# if __name__ == "__main__":
#     asyncio.run()
