from pydantic import Field, ConfigDict
from typing import Annotated
from pydantic import BaseModel
from core.helpers import product_helper
from datetime import datetime


class ProductBase(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=product_helper.NAME_MAX_LEN,
            min_length=product_helper.NAME_MIN_LEN,
        ),
    ]
    description: Annotated[
        str,
        Field(
            max_length=product_helper.DESCRIPTION_MAX_LEN,
            min_length=product_helper.DESCRIPTION_MIN_LEN,
        ),
    ]
    price: Annotated[
        int,
        Field(
            ge=product_helper.PRICE_MIN_VALUE,
        ),
    ]


class Product(ProductBase):
    # «Мостик» между SQLAlchemy ORM объектами и Pydantic схемами
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class ProductCreate(ProductBase):
    pass
