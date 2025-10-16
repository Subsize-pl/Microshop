from typing import Optional, TYPE_CHECKING
from core.helpers import TbHelper
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import Order


class OrderRelationMixin:
    _order_back_populates: Optional[str] = None
    _order_nullable: bool = False

    @declared_attr
    def order_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(f"{TbHelper.generate_tn("Order")}.id"),
            nullable=cls._order_nullable,
        )

    @declared_attr
    def order(cls) -> Mapped["Order"]:
        return relationship(
            "Order",
            back_populates=cls._order_back_populates,
        )
