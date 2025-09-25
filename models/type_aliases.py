from sqlalchemy import text, String
from typing import Annotated, Optional
from datetime import datetime
from sqlalchemy.orm import mapped_column


NameStr = Annotated[
    str,
    mapped_column(String(128), nullable=False),
]

OptionalNameStr = Annotated[
    Optional[str],
    mapped_column(String(128), nullable=True),
]

UsernameStr = Annotated[
    str,
    mapped_column(
        String(128),
        nullable=False,
        unique=True,
    ),
]

EmailStr = Annotated[
    str,
    mapped_column(
        String(320),
        nullable=False,
        unique=True,
    ),
]

PasswordStr = Annotated[
    str,
    mapped_column(
        nullable=False,
    ),
]

CreatedAt = Annotated[
    datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
    ),
]

UpdatedAt = Annotated[
    datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow,
    ),
]
