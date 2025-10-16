from typing import Optional
from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User as UserORM
from core.helpers import db_helper
from auth.jwt_auth import utils
from auth.jwt_auth.scheme import TokenInfo
from routers.users.schemas import User
from core.helpers.password_helper import pwd_helper

jwt_auth_router = APIRouter(prefix="/jwt", tags=["Auth JWT"])


async def validate_user(
    username=Form(),
    password=Form(),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Optional[User]:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

    if user := await session.get(UserORM, username) is None:
        raise unauthed_exc

    if not pwd_helper.verify_password(
        plain_pwd=password,
        hashed_pwd=user.password,
    ):
        raise unauthed_exc

    return user


@jwt_auth_router.post("/login")
async def issue_jwt(
    user: User = Depends(validate_user),
) -> TokenInfo:
    payload = {
        "sub": user.id,
        "username": user.username,
    }
    token: str = utils.encode_jwt(
        payload=payload,
    )
    return TokenInfo(
        access_token=token,
    )
