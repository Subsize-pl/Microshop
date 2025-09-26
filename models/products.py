from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .base import Base
from core.helpers import (
    type_aliases_helper as type_helper,
    product_helper,
)


class Product(Base):
    name: Mapped[str] = mapped_column(
        String(product_helper.NAME_MAX_LEN),
        nullable=product_helper.NAME_MIN_LEN,
    )
    description: Mapped[str] = mapped_column(
        String(product_helper.DESCRIPTION_MAX_LEN),
        nullable=product_helper.DESCRIPTION_MIN_LEN,
    )
    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    created_at: Mapped[type_helper.CreatedAt]
    updated_at: Mapped[type_helper.UpdatedAt]
