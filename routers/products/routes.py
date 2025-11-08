from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import routers.products.crud as crud
from auth.jwt_auth.dependencies import get_active_user_by_access_token
from core.helpers import db_helper
from typing import List, Optional, Annotated
from .schemas import (
    ProductCreate,
    Product,
    ProductUpdate,
    ProductDelete,
)
import routers.products.dependencies as dependencies


router = APIRouter(
    tags=["/products"],
    dependencies=[
        Depends(get_active_user_by_access_token),
    ],
)


@router.get("/", response_model=List[Product])
async def get_products(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Optional[Product])
async def get_product(
    product: Annotated[Product, Depends(dependencies.get_product)],
):
    return product


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Product,
)
async def create_product(
    product_in: ProductCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await crud.create_product(session=session, product_in=product_in)


@router.patch("/{product_id}", response_model=Product)
async def update_product(
    product_update: ProductUpdate,
    product: Annotated[Product, Depends(dependencies.get_product)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_delete: Annotated[ProductDelete, Depends(dependencies.get_product)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    await crud.delete_product(
        session=session,
        product=product_delete,
    )
