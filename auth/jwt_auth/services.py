from typing import Optional, Any, Annotated
from fastapi import Depends, Form, HTTPException, status, Body
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from .utils import decode_jwt
from models.users import User as UserORM
from core.helpers import db_helper
from routers.users.schemas import UserCreate
from jwt.exceptions import InvalidTokenError
from routers.users.schemas import User
from core.helpers import pwd_helper

http_bearer = HTTPBearer()


def get_curr_user_payload(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> dict[str, Any]:
    token = credentials.credentials
    try:
        payload = decode_jwt(jwt_token=token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return payload


async def ensure_unique_user(
    user_in: Annotated[UserCreate, Body],
    session: AsyncSession = Depends(db_helper.session_dependency),
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


async def validate_user_by_form(
    username=Form(),
    password=Form(),
    session: AsyncSession = Depends(db_helper.session_dependency),
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
