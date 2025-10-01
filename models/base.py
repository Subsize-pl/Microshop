from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)
from core.helpers import TbHelper


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return TbHelper.generate_tn(cls.__name__)
