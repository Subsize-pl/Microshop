import uuid
from datetime import timedelta
from auth.jwt_auth.utils import encode_jwt
from core.config import settings
from typing import Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, HTTPException, Depends

from core.helpers import db_helper
from routers.users.schemas import User
from models.users import User as UserORM
from .services import get_curr_user_payload


class TokenFieldHelper:
    SUB_FIELD = "sub"
    TOKEN_TYPE_FIELD = "type"
    JWT_ID_FIELD = "jti"
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    ACCESS_TOKEN_TYPE = "access"
    REFRESH_TOKEN_TYPE = "refresh"


class TokenCreatorHelper:
    @staticmethod
    def _create_jwt(
        token_type: str,
        token_data: dict,
        expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
        expire_timedelta: Optional[timedelta] = None,
    ) -> str:
        payload = {
            token_fields.TOKEN_TYPE_FIELD: token_type,
            token_fields.JWT_ID_FIELD: str(uuid.uuid4()),
        }
        payload.update(token_data)
        return encode_jwt(
            payload=payload,
            expire_minutes=expire_minutes,
            expire_timedelta=expire_timedelta,
        )

    def create_access_token(
        self,
        user: User,
    ) -> str:
        token_data = {
            token_fields.SUB_FIELD: str(user.id),
            token_fields.USERNAME_FIELD: user.username,
        }
        return self._create_jwt(
            token_type=token_fields.ACCESS_TOKEN_TYPE,
            token_data=token_data,
            expire_minutes=settings.auth_jwt.access_token_expire_minutes,
        )

    def create_refresh_token(
        self,
        user: User,
    ) -> str:
        token_data = {
            token_fields.SUB_FIELD: str(user.id),
        }
        return self._create_jwt(
            token_type=token_fields.REFRESH_TOKEN_TYPE,
            token_data=token_data,
            expire_timedelta=timedelta(
                days=settings.auth_jwt.refresh_token_expire_days,
            ),
        )


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

        # Добавить проверку на отсутствие в черном списке

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
            or user.is_superuser != expected_is_superuser
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


token_creator = TokenCreatorHelper()
token_fields = TokenFieldHelper()
