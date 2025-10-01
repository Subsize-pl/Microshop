from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from .base import Base
from core.helpers import product_helper
from core.mixins import TimestampMixin


class Product(TimestampMixin, Base):
    name: Mapped[str] = mapped_column(
        String(product_helper.NAME_MAX_LEN),
        nullable=product_helper.NAME_MIN_LEN,
    )
    description: Mapped[str] = mapped_column(
        String(product_helper.DESCRIPTION_MAX_LEN),
        nullable=product_helper.DESCRIPTION_MIN_LEN,
    )
    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
