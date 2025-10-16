from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from core.mixins import OrderRelationMixin, ProductRelationMixin
from models import Base
from core.helpers import TbHelper


class OrderItem(OrderRelationMixin, ProductRelationMixin, Base):
    # order - product association table
    __tablename__ = "order_items"
    __table_args__ = (
        UniqueConstraint(
            "order_id",
            "product_id",
            name="idx_unique_order_product",
        ),
    )
    _order_back_populates = __tablename__
    _product_back_populates = __tablename__

    quantity: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
        server_default="1",
    )
    unit_price: Mapped[int]
