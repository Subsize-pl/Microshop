from datetime import datetime, timezone
from fastapi import HTTPException
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from models.users import User as UserORM
from core.helpers import pwd_helper
from routers.users.schemas import User, UserCreate, UserUpdate, UserDelete


async def get_user_by_id(
    user_id: int,
    session: AsyncSession,
) -> Optional[User]:
    return await session.get(UserORM, user_id)


async def get_users(
    session: AsyncSession,
) -> List[User]:
    stmt = select(UserORM).order_by(UserORM.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


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


async def update_user(
    user: User,
    user_update: UserUpdate,
    session: AsyncSession,
) -> User:
    for k, v in user_update.model_dump(exclude_unset=True).items():
        setattr(user, k, v)
    user.updated_at = datetime.now(tz=timezone.utc).replace(tzinfo=None)
    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(
    user: UserDelete,
    session: AsyncSession,
) -> None:
    await session.delete(user)
    await session.commit()
