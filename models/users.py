from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from core.helpers import user_helper
from core.mixins import TimestampMixin

if TYPE_CHECKING:
    from models import CartItem, Order


class User(TimestampMixin, Base):
    firstname: Mapped[str] = mapped_column(
        String(user_helper.FIRSTNAME_MAX_LEN),
        nullable=user_helper.FIRSTNAME_NULLABLE,
    )
    lastname: Mapped[str] = mapped_column(
        String(user_helper.LASTNAME_MAX_LEN),
        nullable=user_helper.LASTNAME_NULLABLE,
    )
    username: Mapped[str] = mapped_column(
        String(user_helper.USERNAME_MAX_LEN),
        nullable=user_helper.USERNAME_NULLABLE,
        unique=user_helper.USERNAME_UNIQUE,
    )
    email: Mapped[str] = mapped_column(
        String(user_helper.EMAIL_MAX_LEN),
        nullable=user_helper.EMAIL_NULLABLE,
        unique=user_helper.EMAIL_UNIQUE,
    )
    password_hash: Mapped[str] = mapped_column(
        String(user_helper.HASH_MAX_LEN),
        nullable=user_helper.HASH_NULLABLE,
    )

    cart_items: Mapped[List["CartItem"]] = relationship(
        "CartItem",
        back_populates="user",
    )
    orders: Mapped[List["Order"]] = relationship(
        "Order",
        back_populates="user",
    )
