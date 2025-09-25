from pydantic import BaseModel, Field
from typing import Annotated


NameStr = Annotated[str, Field(max_length=128, min_length=1)]


class Base(BaseModel):
    id: Annotated[int, Field(gt=1)]
