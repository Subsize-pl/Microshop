from fastapi import HTTPException, status
from core.helpers import category_helper
from models import Category as CategoryORM


def validate_category(category_id: int):
    if category_id == category_helper.GENERAL_CATEGORY_ID:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"General category {category_helper.GENERAL_CATEGORY_ID} "
            f"cannot be modified or deleted",
        )


def apply_filter(category_filter: category_helper.CategoryFilter, stmt):
    status_filters = {
        category_helper.CategoryFilter.active: lambda s: s.where(
            CategoryORM.status == category_helper.CategoryStatus.active.value
        ),
        category_helper.CategoryFilter.inactive: lambda s: s.where(
            CategoryORM.status == category_helper.CategoryStatus.inactive.value
        ),
        category_helper.CategoryFilter.all: lambda s: s,
    }

    new_stmt = status_filters.get(category_filter, lambda s: s)(stmt)
    return new_stmt
