from typing import Annotated

from pydantic import Field


class AttributeHelper:
    NAME_MAX_LEN: int = 128
    NAME_NULLABLE: bool = False

    TYPE_STR_MAX_LEN: int = 24
    TYPE_STR_NULLABLE: bool = False


attr_helper = AttributeHelper()
