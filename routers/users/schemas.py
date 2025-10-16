from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from core.helpers import user_helper


class UserBase(BaseModel):
    username: user_helper.UsernameStr
    password: Annotated[
        str,
        Field(min_length=1),
    ]


class UserCreate(UserBase):
    firstname: user_helper.FirstnameStr
    surname: user_helper.SurnameStr
    email: EmailStr


class User(UserCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class UserUpdate(UserBase):  # Partial update
    firstname: Optional[user_helper.FirstnameStr] = None
    surname: Optional[user_helper.SurnameStr] = None
    username: Optional[user_helper.UsernameStr] = None
    email: Optional[EmailStr] = None
    password: Optional[Annotated[str, Field(min_length=1)]] = None


class UserDelete(UserBase):
    pass
