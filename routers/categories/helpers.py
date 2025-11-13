from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from core.helpers import category_helper, db_helper
from . import crud
from .schemas import Category


async def _get_category_dependency(
    category_id: Annotated[int, Path(...)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
) -> Category:
    category_orm = await crud.get_category(
        session=session,
        category_id=category_id,
    )
    if not category_orm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} not found",
        )
    return Category.model_validate(category_orm)


class CategoryGetter:
    def __init__(self, category_filter: category_helper.CategoryFilter):
        self.category_filter = category_filter

    async def __call__(
        self,
        category: Annotated[Category, Depends(_get_category_dependency)],
    ) -> Category:
        if self.category_filter == category_helper.CategoryFilter.all:
            return category

        if (
            self.category_filter == category_helper.CategoryFilter.active
            and category.status == category_helper.CategoryStatus.active
        ) or (
            self.category_filter == category_helper.CategoryFilter.inactive
            and category.status == category_helper.CategoryStatus.inactive
        ):
            return category

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                f"Category validation failed: "
                f"status={category.status}, expected {self.category_filter}"
            ),
        )
