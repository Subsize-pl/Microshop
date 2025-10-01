from datetime import datetime
from typing import Annotated

from black.brackets import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from core.helpers import user_helper


class UserBase(BaseModel):
    firstname: user_helper.FirstnameStr
    surname: user_helper.SurnameStr
    username: user_helper.UsernameStr
    email: EmailStr


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime


class UserCreate(UserBase):
    password: Annotated[
        str,
        Field(min_length=1),
    ]


class UserUpdate(UserBase):  # Partial update
    firstname: Optional[user_helper.FirstnameStrStr] = None
    surname: Optional[user_helper.SurnameStr] = None
    username: Optional[user_helper.UsernameStr] = None
    email: Optional[EmailStr] = None


class UserDelete(UserBase):
    pass
