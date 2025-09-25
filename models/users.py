from sqlalchemy.orm import Mapped
from .base import Base
from .type_aliases import (
    NameStr,
    OptionalNameStr,
    EmailStr,
    UsernameStr,
    PasswordStr,
    CreatedAt,
    UpdatedAt,
)


class User(Base):
    firstname: Mapped[NameStr]
    surname: Mapped[OptionalNameStr]
    username: Mapped[UsernameStr]
    email: Mapped[EmailStr]
    password: Mapped[PasswordStr]
    created_at: Mapped[CreatedAt]
    updated_at: Mapped[UpdatedAt]
