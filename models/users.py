from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from core.helpers import user_helper
from core.mixins import Timestamp


class User(Timestamp, Base):
    firstname: Mapped[str] = mapped_column(
        String(user_helper.FIRSTNAME_MAX_LEN),
        nullable=user_helper.FIRSTNAME_MIN_LEN,
    )
    surname: Mapped[str] = mapped_column(
        String(user_helper.SURNAME_MAX_LEN),
        nullable=user_helper.SURNAME_MIN_LEN,
    )
    username: Mapped[str] = mapped_column(
        String(user_helper.USERNAME_MAX_LEN),
        nullable=user_helper.USERNAME_MIN_LEN,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    password: Mapped[str] = mapped_column(
        nullable=False,
    )
