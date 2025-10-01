from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from models import Product


class ProductRelationMixin:
    _product_back_populates: Optional[str] = None
    _product_nullable: bool = False

    @declared_attr
    def product_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(f"{Product.__table__}.id"),
            nullable=cls._product_nullable,
        )

    @declared_attr
    def product(cls) -> Mapped[Product]:
        return relationship(
            "Product",
            back_populates=cls._product_back_populates,
        )
