from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum as SAEnum
from core.helpers import category_helper
from .base import Base

if TYPE_CHECKING:
    from models import Attribute, Product


class Category(Base):

    # !Category with id = 1 is GLOBAL!

    name: Mapped[str] = mapped_column(
        String(category_helper.MAX_NAME_LEN),
        nullable=category_helper.NAME_NULLABLE,
        unique=category_helper.NAME_UNIQUE,
    )

    status: Mapped[str] = mapped_column(
        SAEnum(category_helper.CategoryStatus, name="category_status"),
        nullable=category_helper.STATUS_NULLABLE,
        server_default=category_helper.STATUS_DEFAULT.value,
    )

    attributes: Mapped[List["Attribute"]] = relationship(
        back_populates="category",
    )

    products: Mapped[List["Product"]] = relationship(
        back_populates="category",
    )
