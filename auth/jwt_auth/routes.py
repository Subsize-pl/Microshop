from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from .services import validate_user, ensure_unique_user, get_curr_user
from fastapi import APIRouter, Depends
from routers.users.crud import create_user
from core.helpers import db_helper, pwd_helper
from auth.jwt_auth import utils
from auth.jwt_auth.scheme import TokenInfo
from routers.users.schemas import User, UserCreate

jwt_auth_router = APIRouter(prefix="/jwt", tags=["Auth JWT"])


@jwt_auth_router.post("/login")
async def issue_jwt(
    user: User = Depends(validate_user),
) -> TokenInfo:
    payload = {
        "sub": str(user.id),
        "username": user.username,
    }
    token: str = utils.encode_jwt(
        payload=payload,
    )
    return TokenInfo(
        access_token=token,
    )


@jwt_auth_router.post("/register")
async def register_user(
    user_in: UserCreate = Depends(ensure_unique_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    return await create_user(
        user_in=user_in,
        session=session,
    )


@jwt_auth_router.get("/me")
async def check_self_info(
    user: User = Depends(get_curr_user),
) -> dict[str, Any]:
    return {
        "username": user.username,
        "email": user.email,
    }
