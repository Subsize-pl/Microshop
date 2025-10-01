from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from core.mixins import (
    ProductRelationMixin,
    AttributeRelationMixin,
)
from models import Base
from core.helpers import TbHelper, product_attr_helper


class ProductAttributes(Base, ProductRelationMixin, AttributeRelationMixin):
    _product_back_populates = f"{TbHelper.generate_tn(__name__)}"
    _attr_nullable = f"{TbHelper.generate_tn(__name__)}"

    value: Mapped[str] = mapped_column(
        String(product_attr_helper.VALUE_STR_LEN),
        nullable=product_attr_helper.VALUE_STR_NULLABLE,
    )
