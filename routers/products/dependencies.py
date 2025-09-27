from typing import Annotated
from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.helpers import db_helper
from . import crud
from .schemas import Product


async def get_product(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    result = await crud.get_product(session=session, product_id=product_id)
    if result is not None:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found",
    )
