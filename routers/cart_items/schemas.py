from typing import Annotated
from core.helpers import cart_item_helper
from pydantic import BaseModel, Field


class CartItemBase(BaseModel):
    quantity: Annotated[
        int,
        Field(
            ge=cart_item_helper.MIN_QUANTITY,
            le=cart_item_helper.MAX_QUANTITY,
        ),
    ]
    product_id: ...


class CartItem(CartItemBase):
    pass
