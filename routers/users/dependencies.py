from typing import Annotated, Optional

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.helpers import db_helper
from models import User
from routers.users import crud


async def get_user_by_id_dependency(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Optional[User]:
    result = await crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if result is not None:
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {user_id} not found",
    )
