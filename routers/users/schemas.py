from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, Field
from core.helpers.model_helpers import user_helper


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
    is_active: bool = user_helper.DEFAULT_IS_ACTIVE
    is_superuser: bool = user_helper.DEFAULT_IS_SUPERUSER
    is_verified: bool = user_helper.DEFAULT_IS_VERIFIED

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
