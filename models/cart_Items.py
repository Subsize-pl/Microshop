from sqlalchemy.orm import Mapped, declared_attr

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

    _user_back_populates = f"{TbHelper.generate_tn(__name__)}"

    quantity: Mapped[int]
