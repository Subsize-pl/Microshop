from typing import Any, Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.helpers.prefixes import Prefixes
from core.helpers.tags import Tags
from .services import ensure_unique_user  # , get_curr_user_payload
from fastapi import APIRouter, Depends, status
from routers.users.crud import create_user
from core.helpers import db_helper
from auth.jwt_auth.scheme import TokenInfo
from routers.users.schemas import User, UserCreate
from .services import validate_user_by_form
from .helpers.token_creator import token_creator
from .helpers.token_fields import TokenFieldHelper
from .helpers.user_getter_by_token import (
    get_active_user_by_access_token,
    get_active_user_by_refresh_token,
)


router = APIRouter(
    prefix=Prefixes.jwt_auth,
    tags=[Tags.jwt_auth],
)


@router.post(
    "/login",
    response_model=TokenInfo,
)
async def issue_jwt(
    user: Annotated[User, Depends(validate_user_by_form)],
):
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    "/refresh",
    response_model=TokenInfo,
)
async def refresh_access_token(
    user: Annotated[User, Depends(get_active_user_by_refresh_token)],
    # cached data -- no problem
    # payload: Annotated[dict, Depends(get_curr_user_payload)],
):
    access_token = token_creator.create_access_token(user)
    refresh_token = token_creator.create_refresh_token(user)

    # TODO: implement adding the old token to the blacklist

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
)
async def register_user(
    user_in: Annotated[UserCreate, Depends(ensure_unique_user)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await create_user(
        user_in=user_in,
        session=session,
    )


@router.get(
    "/me",
    response_model=dict[str, Any],
)
async def check_self_info(
    user: Annotated[User, Depends(get_active_user_by_access_token)],
):
    return {
        TokenFieldHelper.USERNAME_FIELD: user.username,
        TokenFieldHelper.EMAIL_FIELD: user.email,
    }
