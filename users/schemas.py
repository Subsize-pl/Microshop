from .base import Base, NameStr
from pydantic import Field, EmailStr


class UserCreate(Base):
    firstname: NameStr
    surname: NameStr
    username: NameStr
    email: EmailStr
    password: str
