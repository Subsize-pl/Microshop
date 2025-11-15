import uuid
from datetime import timedelta
from typing import Optional

from auth.jwt_auth.helpers.token_fields import TokenFieldHelper
from auth.jwt_auth.utils import encode_jwt
from core.config import settings
from routers.users.schemas import User


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


token_creator = TokenCreatorHelper()
token_fields = TokenFieldHelper()
