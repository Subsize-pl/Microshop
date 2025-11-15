from typing import Annotated, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import InvalidTokenError
from auth.jwt_auth.utils import decode_jwt

http_bearer = HTTPBearer()


def get_curr_user_payload(
    credentials: Annotated[
        HTTPAuthorizationCredentials,
        Depends(http_bearer),
    ],
) -> dict[str, Any]:
    token = credentials.credentials
    try:
        payload = decode_jwt(jwt_token=token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return payload
