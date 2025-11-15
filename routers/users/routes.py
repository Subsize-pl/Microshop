from typing import Annotated, Optional
from auth.jwt_auth.helpers.user_getter_by_token import (
    get_active_user_by_access_token,
    get_active_superuser_by_access_token,
)
from core.helpers.prefixes import Prefixes
from core.helpers.tags import Tags
from models import User as UserORM
from routers.users import crud
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.helpers import db_helper
from routers.products import crud
from routers.users.dependencies import get_user_by_id_dependency
from routers.users.schemas import UserUpdate, UserDelete, User

router = APIRouter(
    prefix=Prefixes.users,
    tags=[Tags.users],
)


@router.get(
    path="/",
    dependencies=[Depends(get_active_superuser_by_access_token)],
)
async def get_users(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
):
    return await crud.get_users(
        session=session,
    )


@router.get(
    path="/{user_id}",
    dependencies=Depends(get_active_superuser_by_access_token),
    response_model=Optional[User],
)
async def get_user_by_id(
    user: Annotated[UserORM, get_user_by_id_dependency],
):
    return user


@router.patch(
    path="/update",
    response_model=User,
)
async def update_product(
    user: Annotated[UserORM, Depends(get_active_user_by_access_token)],
    user_update: UserUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.delete(
    path="/delete",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_delete: UserDelete,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    await crud.delete_user(
        session=session,
        user=user_delete,
    )
