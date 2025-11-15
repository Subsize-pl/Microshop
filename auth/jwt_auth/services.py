from typing import Optional, Annotated
from fastapi import Depends, Form, HTTPException, status, Body
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User as UserORM
from core.helpers import db_helper
from routers.users.schemas import UserCreate, User
from core.helpers import pwd_helper


async def validate_user_by_form(
    username: Annotated[
        str,
        Form(examples=["username"]),
    ],
    password: Annotated[
        str,
        Form(examples=["password"]),
    ],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
) -> Optional[User]:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

    stmt = select(UserORM).where(UserORM.username == username)
    result = await session.execute(stmt)

    if (user := result.scalar_one_or_none()) is None:
        raise unauthed_exc

    if not pwd_helper.verify_password(
        plain_pwd=password,
        hashed_pwd=user.password_hash,
    ):
        raise unauthed_exc

    return user


async def ensure_unique_user(
    user_in: Annotated[UserCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> Optional[UserCreate]:
    conditions = [UserORM.username == user_in.username]

    if user_in.email is not None:
        conditions.append(UserORM.email == user_in.email)

    stmt = select(UserORM).where(or_(*conditions))
    existing_user = await session.scalar(stmt)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already taken",
        )

    return user_in
