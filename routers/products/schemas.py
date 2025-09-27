from pydantic import Field, ConfigDict
from typing import Annotated, Optional
from pydantic import BaseModel
from core.helpers import product_helper
from datetime import datetime


class ProductBase(BaseModel):
    name: product_helper.NameStr
    description: product_helper.DescriptionStr
    price: product_helper.PriceInt


class Product(ProductBase):
    # «Мостик» между SQLAlchemy ORM объектами и Pydantic схемами
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):  # Partial update
    name: Optional[product_helper.NameStr] = None
    description: Optional[product_helper.DescriptionStr] = None
    price: Optional[product_helper.PriceInt] = None


class ProductDelete(ProductBase):
    pass
