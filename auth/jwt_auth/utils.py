from datetime import timedelta, datetime, timezone
from typing import Any, Optional
import jwt
from core.config import settings


def encode_jwt(
    payload: dict[str, Any],
    private_key: str = settings.auth_jwt.private_key,
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: Optional[timedelta] = None,
) -> str:
    now = datetime.now(timezone.utc)
    ext_payload = payload.copy()
    if expire_timedelta is not None:
        expire_time = now + expire_timedelta
    else:
        expire_time = now + timedelta(minutes=expire_minutes)

    ext_payload.update(
        exp=expire_time,
        iat=now,
    )
    encoded = jwt.encode(
        payload=ext_payload,
        key=private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    jwt_token: str | bytes,
    public_key: str = settings.auth_jwt.public_key,
    algorithm: str = settings.auth_jwt.algorithm,
) -> dict[str, Any]:
    decoded = jwt.decode(
        jwt=jwt_token,
        key=public_key,
        algorithms=[algorithm],
    )
    return decoded
