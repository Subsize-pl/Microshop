from typing import Annotated

from pydantic import Field


class ProductHelper:
    NAME_MAX_LEN: int = 128
    NAME_MIN_LEN: int = 1

    DESCRIPTION_MAX_LEN: int = 1024
    DESCRIPTION_MIN_LEN: int = 0

    PRICE_MAX_VALUE: int | None = None
    PRICE_MIN_VALUE = 1
    DISCOUNT_PRICE_NULLABLE: bool = True

    NameStr = Annotated[
        str,
        Field(
            max_length=NAME_MAX_LEN,
            min_length=NAME_MIN_LEN,
        ),
    ]

    DescriptionStr = Annotated[
        str,
        Field(
            max_length=DESCRIPTION_MAX_LEN,
            min_length=DESCRIPTION_MIN_LEN,
        ),
    ]

    PriceInt = Annotated[
        int,
        Field(
            ge=PRICE_MIN_VALUE,
        ),
    ]

    NAME_NULLABLE: bool = NAME_MIN_LEN == 0
    DESCRIPTION_NULLABLE: bool = DESCRIPTION_MIN_LEN == 0


product_helper = ProductHelper()
