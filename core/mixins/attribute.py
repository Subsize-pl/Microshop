from typing import Optional, TYPE_CHECKING
from core.helpers import TbHelper
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import Attribute


class AttributeRelationMixin:
    _attr_back_populates: Optional[str] = None
    _attr_nullable: bool = False

    @declared_attr
    def attribute_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(f"{TbHelper.generate_tn("Attribute")}.id"),
            nullable=cls._attr_nullable,
        )

    @declared_attr
    def attribute(cls) -> Mapped["Attribute"]:
        return relationship(
            "Attribute",
            back_populates=cls._attr_back_populates,
        )
