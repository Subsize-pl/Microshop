from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from core.mixins import (
    ProductRelationMixin,
    UserRelationMixin,
)
from models import Base
from core.helpers import TbHelper


class CartItem(ProductRelationMixin, UserRelationMixin, Base):
    @declared_attr
    def _product_back_populates(cls):
        return TbHelper.generate_tn(cls)

    @declared_attr
    def _user_back_populates(cls):
        return TbHelper.generate_tn(cls)

    quantity: Mapped[int] = mapped_column(nullable=False)
