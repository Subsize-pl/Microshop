from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from core.helpers import attr_helper
from core.mixins.category import CategoryRelationMixin
from models import Base


class Attribute(CategoryRelationMixin, Base):
    __tablename__ = "attributes"
    _category_back_populates = f"{__tablename__}"
    _category_nullable = True  # For common products

    name: Mapped[str] = mapped_column(
        String(attr_helper.NAME_MAX_LEN),
        nullable=attr_helper.NAME_NULLABLE,
    )
    type: Mapped[str] = mapped_column(
        String(attr_helper.NAME_MAX_LEN),
        nullable=attr_helper.NAME_NULLABLE,
    )
