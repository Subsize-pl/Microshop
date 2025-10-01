from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from core.mixins import OrderRelationMixin, ProductRelationMixin
from models import Base
from core.helpers import TbHelper


class OrderItem(OrderRelationMixin, ProductRelationMixin, Base):
    @declared_attr
    def _order_back_populates(cls):
        return TbHelper.generate_tn(cls)

    @declared_attr
    def _product_back_populates(cls):
        return TbHelper.generate_tn(cls)

    quantity: Mapped[int] = mapped_column(nullable=False)
