from datetime import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column


class TypeAliasesHelper:
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

type_aliases_helper = TypeAliasesHelper()

