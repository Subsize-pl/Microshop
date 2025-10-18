from fastapi import HTTPException
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from models.users import User as UserORM
from core.helpers import pwd_helper
from routers.users.schemas import User, UserCreate


async def create_user(
    user_in: UserCreate,
    session: AsyncSession,
) -> User:
    user = UserORM(**user_in.model_dump(exclude={"password"}))
    user.password_hash = pwd_helper.hash_password(user_in.password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_user_by_id(
    user_id: int,
    session: AsyncSession,
) -> Optional[User]:
    if user := await session.get(UserORM, user_id):
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User not found",
    )
