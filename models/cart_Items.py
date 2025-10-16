from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from core.mixins import (
    ProductRelationMixin,
    UserRelationMixin,
)
from models import Base
from core.helpers import TbHelper


class CartItem(ProductRelationMixin, UserRelationMixin, Base):
    __tablename__ = "cart_items"

    @declared_attr
    def _product_back_populates(cls):
        return cls.__tablename__

    @declared_attr
    def _user_back_populates(cls):
        return cls.__tablename__

    quantity: Mapped[int] = mapped_column(nullable=False)
