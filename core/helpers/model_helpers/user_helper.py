from typing import Annotated, Optional
from pydantic import Field


class UserHelper:
    FIRSTNAME_MAX_LEN: int = 128
    FIRSTNAME_MIN_LEN: int = 1
    FIRSTNAME_NULLABLE: bool = False

    LASTNAME_MAX_LEN: int = 128
    LASTNAME_MIN_LEN: int = 1
    LASTNAME_NULLABLE: bool = False

    USERNAME_MAX_LEN: int = 128
    USERNAME_MIN_LEN: int = 1
    USERNAME_NULLABLE: bool = False
    USERNAME_UNIQUE: bool = True

    EMAIL_MAX_LEN: int = 256  # RFC рекомендует до 254 символов
    EMAIL_NULLABLE: bool = False
    EMAIL_UNIQUE: bool = False

    HASH_MAX_LEN: int = 128  # достаточно для bcrypt
    HASH_NULLABLE: bool = False

    FirstnameStr = Annotated[
        Optional[str] if FIRSTNAME_NULLABLE else str,
        Field(
            min_length=FIRSTNAME_MIN_LEN,
            max_length=FIRSTNAME_MAX_LEN,
        ),
    ]

    SurnameStr = Annotated[
        Optional[str] if LASTNAME_NULLABLE else str,
        Field(
            min_length=LASTNAME_MIN_LEN,
            max_length=LASTNAME_MAX_LEN,
        ),
    ]

    UsernameStr = Annotated[
        Optional[str] if USERNAME_NULLABLE else str,
        Field(
            min_length=USERNAME_MIN_LEN,
            max_length=USERNAME_MAX_LEN,
        ),
    ]


user_helper = UserHelper()
