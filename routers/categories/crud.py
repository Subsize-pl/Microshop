from datetime import datetime, timezone
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from core.helpers import category_helper
from models.categories import Category as CategoryORM
from typing import List, Optional
from .schemas import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
)
from .utils import apply_filter, validate_category
from routers.users.schemas import User


async def get_filtered_categories(
    session: AsyncSession,
    category_filter: category_helper.CategoryFilter,
) -> List[CategoryORM]:
    """
    Retrieve categories from the database with optional filtering by activity.

    :param session: Async database session.
    :param category_filter:
        - ACTIVE — return only active categories
        - INACTIVE — return only inactive categories
        - ALL — return all categories
    :return: List of CategoryORM objects.
    """

    stmt = select(CategoryORM).order_by(CategoryORM.id)

    stmt = apply_filter(category_filter, stmt)

    result: Result = await session.execute(stmt)
    categories = result.scalars().all()

    return list(categories)


async def get_filtered_categories_after_validation(
    category_filter: category_helper.CategoryFilter,
    current_user: User,
    session: AsyncSession,
) -> Optional[List[CategoryORM]]:
    if (
        category_filter != category_helper.CategoryFilter.active
        and not current_user.is_superuser
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only superusers can see all categories",
        )

    categories = await get_filtered_categories(
        session=session,
        category_filter=category_filter,
    )

    return categories


async def get_category(
    category_id: int,
    session: AsyncSession,
) -> Optional[CategoryORM]:
    return await session.get(CategoryORM, category_id)


async def create_category(
    session: AsyncSession,
    category_in: CategoryCreate,
) -> CategoryORM:
    category = CategoryORM(**category_in.model_dump())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category


async def update_category(
    category: Category,
    category_update: CategoryUpdate,
    session: AsyncSession,
) -> CategoryORM:
    validate_category(category_id=category.id)
    for k, v in category_update.model_dump(exclude_unset=True).items():
        setattr(category, k, v)
    category.updated_at = datetime.now(tz=timezone.utc).replace(tzinfo=None)
    await session.commit()
    await session.refresh(category)
    return category


async def delete_category(
    category: CategoryDelete,
    session: AsyncSession,
) -> None:
    await session.delete(category)
    await session.commit()
