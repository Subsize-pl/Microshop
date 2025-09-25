from .base import Base, NameStr
from pydantic import Field, EmailStr
from typing import Optional


class UserCreate(Base):
    firstname: NameStr
    surname: Optional[NameStr]
    username: NameStr
    email: EmailStr
    password: str
