from .base import Base, NameStr
from pydantic import Field, EmailStr
from typing import Optional, Annotated


class UserBase(Base):
    firstname: NameStr
    surname: Optional[NameStr]
    username: NameStr
    email: EmailStr
    password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: Annotated[int, Field(gt=1)]


class UserDelete(User):
    pass


class UserUpdatePartial(UserBase):
    firstname: Optional[NameStr] = None
    surname: Optional[NameStr] = None
    username: Optional[NameStr] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserUpdate(UserBase):
    pass
