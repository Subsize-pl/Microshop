from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict

from core.helpers import category_helper


class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[
        str,
        Field(
            max_length=category_helper.MAX_NAME_LEN,
            min_length=category_helper.MIN_NAME_LEN,
        ),
    ]


class Category(CategoryBase):
    id: int
    status: category_helper.CategoryStatus


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    is_active: bool


class CategoryDelete(BaseModel):
    id: int
