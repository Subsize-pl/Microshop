from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from core.helpers import category_helper
from .base import Base

if TYPE_CHECKING:
    from models import Attribute, Product


class Category(Base):

    # !Category with id = 1 is GLOBAL!

    name: Mapped[str] = mapped_column(
        String(category_helper.MAX_NAME_LEN),
        nullable=category_helper.NAME_NULLABLE,
    )

    attributes: Mapped[List["Attribute"]] = relationship(
        back_populates="category",
    )

    products: Mapped[List["Product"]] = relationship(
        back_populates="category",
    )
