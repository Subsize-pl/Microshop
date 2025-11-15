from enum import StrEnum


class Prefixes(StrEnum):
    categories = "/categories"
    products = "/products"
    cart_items = "/cart_items"

    users = "/users"
    jwt_auth = "/auth"
