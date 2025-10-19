from typing import Optional

from pydantic import BaseModel


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    content_type: str = "Bearer"
