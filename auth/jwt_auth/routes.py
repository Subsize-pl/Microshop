from typing import Any, Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from .services import ensure_unique_user, get_curr_user_payload
from fastapi import APIRouter, Depends
from routers.users.crud import create_user
from core.helpers import db_helper
from auth.jwt_auth.scheme import TokenInfo
from routers.users.schemas import User, UserCreate
from .services import validate_user_by_form
from .helpers import token_creator
from .dependencies import (
    get_active_user_by_access_token,
    get_active_user_by_refresh_token,
    token_fields,
)

jwt_auth_router = APIRouter(prefix="/jwt", tags=["Auth JWT"])


@jwt_auth_router.post("/login", response_model=TokenInfo)
async def issue_jwt(
    user: Annotated[User, Depends(validate_user_by_form)],
):
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@jwt_auth_router.post("/refresh", response_model=TokenInfo)
async def refresh_access_token(
    user: Annotated[User, Depends(get_active_user_by_refresh_token)],
    # cached data -- no problem
    payload: Annotated[dict, Depends(get_curr_user_payload)],
):
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    # Добавление старого токена в черный список

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@jwt_auth_router.post("/register", response_model=User)
async def register_user(
    user_in: Annotated[UserCreate, Depends(ensure_unique_user)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await create_user(
        user_in=user_in,
        session=session,
    )


@jwt_auth_router.get("/me")
async def check_self_info(
    user: Annotated[User, Depends(get_active_user_by_access_token)],
) -> dict[str, Any]:
    return {
        token_fields.USERNAME_FIELD: user.username,
        token_fields.EMAIL_FIELD: user.email,
    }
