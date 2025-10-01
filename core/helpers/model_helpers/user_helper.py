from typing import Annotated

from pydantic import Field


class UserHelper:
    FIRSTNAME_MAX_LEN = 128
    FIRSTNAME_MIN_LEN = 1

    SURNAME_MAX_LEN = 128
    SURNAME_MIN_LEN = 0

    USERNAME_MAX_LEN = 128
    USERNAME_MIN_LEN = 1

    FirstnameStr = Annotated[
        str,
        Field(
            min_length=FIRSTNAME_MIN_LEN,
            max_length=FIRSTNAME_MAX_LEN,
        ),
    ]

    SurnameStr = Annotated[
        str,
        Field(
            min_length=SURNAME_MIN_LEN,
            max_length=SURNAME_MAX_LEN,
        ),
    ]

    UsernameStr = Annotated[
        str,
        Field(
            min_length=USERNAME_MIN_LEN,
            max_length=USERNAME_MAX_LEN,
        ),
    ]


user_helper = UserHelper()
