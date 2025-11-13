from typing import Annotated, Optional, List
from auth.jwt_auth.dependencies import (
    get_active_superuser_by_access_token,
    get_active_user_by_access_token,
)
from routers.categories import crud
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from core.helpers import db_helper, category_helper
from .dependencies import (
    get_active_category,
    get_any_category,
)
from .schemas import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
)
from .utils import validate_category
from routers.users.schemas import User

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.get(
    path="/",
    response_model=List[Category],
)
async def get_categories(
    current_user: Annotated[
        User,
        Depends(get_active_user_by_access_token),
    ],
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_dependency),
    ],
    category_filter: Annotated[
        category_helper.CategoryFilter,
        Query(),
    ] = category_helper.CategoryFilter.active,
):
    categories_orm = await crud.get_filtered_categories_after_validation(
        category_filter=category_filter,
        current_user=current_user,
        session=session,
    )

    return [Category.model_validate(c) for c in categories_orm]


@router.get(
    path="/{category_id}",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    response_model=Optional[Category],
)
async def get_category(
    category: Annotated[Category, Depends(get_any_category)],
):
    return category


@router.post(
    path="/create",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    status_code=status.HTTP_201_CREATED,
    response_model=Category,
)
async def create_product(
    category_in: CategoryCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    new_category_orm = await crud.create_category(
        category_in=category_in,
        session=session,
    )
    new_category = Category.model_validate(new_category_orm)
    return new_category


@router.patch(
    path="/update/{category_id}",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    response_model=Category,
)
async def update_category(
    category: Annotated[Category, Depends(get_any_category)],
    category_update: CategoryUpdate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    updated_category_orm = await crud.update_category(
        category=category,
        category_update=category_update,
        session=session,
    )
    return Category.model_validate(updated_category_orm)


@router.delete(
    path="/delete/{category_id}",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_user(
    category_delete: Annotated[Category, Depends(get_active_category)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    validate_category(category_id=category_delete.id)
    await crud.delete_category(
        category=CategoryDelete(**category_delete.model_dump()),
        session=session,
    )
