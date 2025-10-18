from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from core.helpers import user_helper


class UserBase(BaseModel):
    username: user_helper.UsernameStr


class UserCreate(UserBase):
    firstname: user_helper.FirstnameStr
    lastname: user_helper.LastnameStr
    email: user_helper.UserEmailStr
    password: Annotated[
        str,
        Field(min_length=1),
    ]


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    firstname: user_helper.FirstnameStr
    lastname: user_helper.LastnameStr
    email: user_helper.UserEmailStr
    created_at: datetime
    updated_at: datetime


class UserUpdate(UserBase):  # Partial update
    firstname: Optional[user_helper.FirstnameStr] = None
    lastname: Optional[user_helper.LastnameStr] = None
    username: Optional[user_helper.UsernameStr] = None
    email: Optional[user_helper.UserEmailStr] = None
    password: Optional[Annotated[str, Field(min_length=1)]] = None


class UserDelete(UserBase):
    pass
