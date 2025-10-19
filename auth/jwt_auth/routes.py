from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from .services import ensure_unique_user, get_curr_user_payload
from fastapi import APIRouter, Depends
from routers.users.crud import create_user
from core.helpers import db_helper
from auth.jwt_auth.scheme import TokenInfo
from routers.users.schemas import User, UserCreate
from .services import validate_user_by_form
from .helpers import (
    token_creator,
    get_user_by_access_token,
    get_user_by_refresh_token,
    token_fields,
)

jwt_auth_router = APIRouter(prefix="/jwt", tags=["Auth JWT"])


@jwt_auth_router.post("/login")
async def issue_jwt(
    user: User = Depends(validate_user_by_form),
) -> TokenInfo:
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@jwt_auth_router.post("/refresh")
async def refresh_access_token(
    user: User = Depends(get_user_by_refresh_token),
    # cached data -- no problem
    payload: dict = Depends(get_curr_user_payload),
) -> TokenInfo:
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    # Добавление старого токена в черный список

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
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
    user: User = Depends(get_user_by_access_token),
) -> dict[str, Any]:
    return {
        token_fields.USERNAME_FIELD: user.username,
        token_fields.EMAIL_FIELD: user.email,
    }
