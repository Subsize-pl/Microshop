from typing import Any, Optional
from fastapi import HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from auth.jwt_auth.dependencies import get_curr_user_payload
from auth.jwt_auth.helpers.token_creator import token_fields
from core.helpers import db_helper
from models import User as UserORM
from routers.users.schemas import User


class UserGetterByToken:
    def __init__(
        self,
        token_type: str,
        is_active: bool,
        is_superuser: bool,
        is_verified: bool,
    ):
        self.token_type = token_type
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.is_verified = is_verified

    @staticmethod
    async def _get_user_by_sub(
        payload: dict[str, Any],
        session: AsyncSession,
    ) -> Optional[User]:
        if user := await session.get(
            UserORM,
            int(payload.get(token_fields.SUB_FIELD, 0)),
        ):
            return user

        # TODO: Add a check for absence from the blacklist

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token",
        )

    @staticmethod
    def _validate_token_type(
        payload: dict[str, Any],
        expected_token_type: str,
    ) -> None:
        curr_token_type: str = payload.get(token_fields.TOKEN_TYPE_FIELD)
        if curr_token_type != expected_token_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"expected {expected_token_type!r} token type but found {curr_token_type!r}",
            )

    @staticmethod
    def _validate_user(
        user: User,
        expected_is_active: bool,
        expected_is_superuser: bool,
        expected_is_verified: bool,
    ) -> None:

        if (
            user.is_active != expected_is_active
            or (user.is_superuser != expected_is_superuser and not user.is_superuser)
            or user.is_verified != expected_is_verified
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    "User validation failed: "
                    f"is_active={user.is_active}, expected={expected_is_active}; "
                    f"is_superuser={user.is_superuser}, expected={expected_is_superuser}; "
                    f"is_verified={user.is_verified}, expected={expected_is_verified}"
                ),
            )

    async def __call__(
        self,
        payload: dict = Depends(get_curr_user_payload),
        session: AsyncSession = Depends(db_helper.session_dependency),
    ) -> Optional[User]:
        self._validate_token_type(
            payload=payload,
            expected_token_type=self.token_type,
        )
        user = await self._get_user_by_sub(
            payload=payload,
            session=session,
        )
        self._validate_user(
            user=user,
            expected_is_active=self.is_active,
            expected_is_superuser=self.is_superuser,
            expected_is_verified=self.is_verified,
        )
        return user


get_active_user_by_access_token = UserGetterByToken(
    token_type=token_fields.ACCESS_TOKEN_TYPE,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)
get_active_user_by_refresh_token = UserGetterByToken(
    token_type=token_fields.REFRESH_TOKEN_TYPE,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)
get_active_superuser_by_access_token = UserGetterByToken(
    token_type=token_fields.ACCESS_TOKEN_TYPE,
    is_active=True,
    is_superuser=True,
    is_verified=True,
)
get_active_superuser_by_refresh_token = UserGetterByToken(
    token_type=token_fields.REFRESH_TOKEN_TYPE,
    is_active=True,
    is_superuser=True,
    is_verified=True,
)
