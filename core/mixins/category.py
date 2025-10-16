from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import relationship, Mapped, declared_attr, mapped_column
from sqlalchemy import ForeignKey
from core.helpers import TbHelper

if TYPE_CHECKING:
    from models import Category


class CategoryRelationMixin:
    _category_back_populates: Optional[str] = None
    _category_nullable: bool = False

    @declared_attr
    def category_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(f"{TbHelper.generate_tn('Category')}.id"),
            nullable=cls._category_nullable,
        )

    @declared_attr
    def category(cls) -> Mapped["Category"]:
        return relationship(
            "Category",
            back_populates=cls._category_back_populates,
        )
