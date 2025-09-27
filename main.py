from fastapi import FastAPI
from products import router
import asyncio


app = FastAPI()
app.include_router(router=router)


# if __name__ == "__main__":
#     asyncio.run()
