from sqlalchemy.orm import Mapped

from core.mixins import (
    ProductRelationMixin,
    UserRelationMixin,
)
from models import Base
from core.helpers import TbHelper


class CartItems(ProductRelationMixin, UserRelationMixin, Base):
    _product_back_populates = f"{TbHelper.generate_tn(__name__)}"
    _user_back_populates = f"{TbHelper.generate_tn(__name__)}"

    quantity: Mapped[int]
