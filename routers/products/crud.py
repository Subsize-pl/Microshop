from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from models.products import Product as ProductORM
from typing import List, Optional
from .schemas import (
    Product,
    ProductCreate,
)


async def get_products(session: AsyncSession) -> List[Product]:
    stmt = select(ProductORM).order_by(ProductORM.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(
    session: AsyncSession,
    product_id: int,
) -> Optional[Product]:
    return await session.get(ProductORM, product_id)


async def create_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    product = ProductORM(**product_in.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
