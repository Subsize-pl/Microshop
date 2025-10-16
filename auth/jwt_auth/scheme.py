from pydantic import BaseModel


class TokenInfo(BaseModel):
    access_token: str
    content_type: str = "Bearer"
