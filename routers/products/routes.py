from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import routers.products.crud as crud
from auth.jwt_auth.helpers.user_getter_by_token import (
    get_active_user_by_access_token,
    get_active_superuser_by_access_token,
)
from core.helpers import db_helper
from typing import List, Optional, Annotated

from core.helpers.prefixes import Prefixes
from core.helpers.tags import Tags
from .schemas import (
    ProductCreate,
    Product,
    ProductUpdate,
    ProductDelete,
)
import routers.products.dependencies as dependencies

router = APIRouter(
    prefix=Prefixes.products,
    tags=[Tags.products],
)


@router.get(
    path="/",
    response_model=List[Product],
)
async def get_products(
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    return await crud.get_products(session=session)


@router.get(
    path="/{product_id}",
    response_model=Optional[Product],
)
async def get_product(
    product: Annotated[Product, Depends(dependencies.get_product_dependency)],
):
    return product


@router.post(
    path="/create",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    status_code=status.HTTP_201_CREATED,
    response_model=Product,
)
async def create_product(
    product_in: ProductCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    new_product_orm = await crud.create_product(
        session=session,
        product_in=product_in,
    )
    new_product = Product.model_validate(new_product_orm)
    return new_product


@router.patch(
    path="/{product_id}",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    response_model=Product,
)
async def update_product(
    product_update: ProductUpdate,
    product: Annotated[Product, Depends(dependencies.get_product_dependency)],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    new_product_orm = await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )

    new_product = Product.model_validate(new_product_orm)
    return new_product


@router.delete(
    path="/{product_id}",
    dependencies=[Depends(get_active_superuser_by_access_token)],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(
    product_delete: Annotated[
        ProductDelete,
        Depends(dependencies.get_product_dependency),
    ],
    session: Annotated[AsyncSession, Depends(db_helper.session_dependency)],
):
    await crud.delete_product(
        session=session,
        product=product_delete,
    )
