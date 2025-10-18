from typing import Annotated, Optional
from pydantic import Field, EmailStr


class UserHelper:
    FIRSTNAME_MAX_LEN: int = 128
    FIRSTNAME_MIN_LEN: int = 1
    FIRSTNAME_NULLABLE: bool = False

    LASTNAME_MAX_LEN: int = 128
    LASTNAME_MIN_LEN: int = 1
    LASTNAME_NULLABLE: bool = True

    USERNAME_MAX_LEN: int = 128
    USERNAME_MIN_LEN: int = 1
    USERNAME_NULLABLE: bool = False
    USERNAME_UNIQUE: bool = True

    EMAIL_MAX_LEN: int = 256  # RFC рекомендует до 254 символов
    EMAIL_NULLABLE: bool = False
    EMAIL_UNIQUE: bool = True

    HASH_MAX_LEN: int = 128  # достаточно для bcrypt
    HASH_NULLABLE: bool = False

    @staticmethod
    def StrField(nullable: bool, min_len: int, max_len: int):
        return Annotated[
            Optional[str] if nullable else str,
            Field(
                min_length=min_len,
                max_length=max_len,
                default=None if nullable else ...,
            ),
        ]

    @staticmethod
    def EmailField(nullable: bool):
        return Annotated[
            Optional[EmailStr] if nullable else EmailStr,
            Field(
                default=None if nullable else ...,
            ),
        ]

    FirstnameStr = StrField(
        FIRSTNAME_NULLABLE,
        FIRSTNAME_MIN_LEN,
        FIRSTNAME_MAX_LEN,
    )
    LastnameStr = StrField(
        LASTNAME_NULLABLE,
        LASTNAME_MIN_LEN,
        LASTNAME_MAX_LEN,
    )
    UsernameStr = StrField(
        USERNAME_NULLABLE,
        USERNAME_MIN_LEN,
        USERNAME_MAX_LEN,
    )
    UserEmailStr = EmailField(EMAIL_NULLABLE)


user_helper = UserHelper()
