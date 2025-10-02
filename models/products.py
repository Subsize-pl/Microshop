from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, CheckConstraint
from .base import Base
from core.helpers import product_helper
from core.mixins import TimestampMixin, CategoryRelationMixin

if TYPE_CHECKING:
    from models import OrderItem


class Product(TimestampMixin, CategoryRelationMixin, Base):
    __table_args__ = (
        CheckConstraint(
            f"price >= {product_helper.PRICE_MIN_VALUE} AND discount_price >= {product_helper.PRICE_MIN_VALUE}",
            name="check_price_positive",
        ),
    )

    name: Mapped[str] = mapped_column(
        String(product_helper.NAME_MAX_LEN),
        nullable=product_helper.NAME_NULLABLE,
    )

    description: Mapped[str] = mapped_column(
        String(product_helper.DESCRIPTION_MAX_LEN),
        nullable=product_helper.DESCRIPTION_NULLABLE,
    )

    price: Mapped[int]

    discount_price: Mapped[int] = mapped_column(
        Integer,
        nullable=product_helper.DISCOUNT_PRICE_NULLABLE,
    )

    order_items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="product",
    )
