from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, declared_attr

from core.mixins import (
    ProductRelationMixin,
    AttributeRelationMixin,
)
from models import Base
from core.helpers import TbHelper, product_attr_helper


class ProductAttribute(Base, ProductRelationMixin, AttributeRelationMixin):
    __tablename__ = "product_attributes"

    @declared_attr
    def _product_back_populates(cls):
        return cls.__tablename__

    @declared_attr
    def _attr_back_populates(cls):
        return cls.__tablename__

    value: Mapped[str] = mapped_column(
        String(product_attr_helper.VALUE_STR_LEN),
        nullable=product_attr_helper.VALUE_STR_NULLABLE,
    )
