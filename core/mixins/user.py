from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from core.helpers import TbHelper

if TYPE_CHECKING:
    from models import User


class UserRelationMixin:
    _user_nullable: bool = False
    _user_back_populates: Optional[str] = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey(f"{TbHelper.generate_tn("User")}.id"),
            nullable=cls._user_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )
