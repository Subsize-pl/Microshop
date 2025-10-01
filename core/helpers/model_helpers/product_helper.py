from typing import Annotated

from pydantic import Field


class ProductHelper:
    NAME_MAX_LEN = 128
    NAME_MIN_LEN = 1

    DESCRIPTION_MAX_LEN = 1024
    DESCRIPTION_MIN_LEN = 0

    PRICE_MAX_VALUE = None
    PRICE_MIN_VALUE = 1

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


product_helper = ProductHelper()
