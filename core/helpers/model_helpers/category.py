from enum import Enum


class CategoryHelper:
    GENERAL_CATEGORY_ID = 1

    MAX_NAME_LEN: int = 128
    MIN_NAME_LEN: int = 1
    NAME_NULLABLE: bool = False
    NAME_UNIQUE: bool = True

    class CategoryStatus(str, Enum):
        active = "active"
        inactive = "inactive"

    class CategoryFilter(str, Enum):
        active = "active"
        inactive = "inactive"
        all = "all"

    STATUS_NULLABLE: bool = False
    STATUS_DEFAULT: CategoryStatus = CategoryStatus.active


category_helper = CategoryHelper()
