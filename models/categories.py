from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from core.helpers import category_helper
from .base import Base


class Category(Base):
    name: Mapped[str] = mapped_column(
        String(category_helper.MAX_NAME_LEN),
        nullable=category_helper.MIN_NAME_LEN
    )
