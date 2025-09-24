from .base import Base, NameStr, PasswordStr
from pydantic import Field, EmailStr
from typing import Annotated


class UserCreate(Base):
    firstname: NameStr
    surname: NameStr
    username: NameStr
    email: EmailStr
    password: PasswordStr
