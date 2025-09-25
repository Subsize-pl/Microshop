from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import Base, User
from db_utils import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
