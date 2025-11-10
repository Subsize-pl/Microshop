class CategoryHelper:
    GENERAL_CATEGORY_ID = 1

    MAX_NAME_LEN: int = 128
    MIN_NAME_LEN: int = 1
    NAME_NULLABLE: bool = False
    NAME_UNIQUE: bool = True


category_helper = CategoryHelper()
