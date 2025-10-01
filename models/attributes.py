from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, declared_attr
from core.helpers import attr_helper, TbHelper
from core.mixins.category import CategoryRelationMixin
from models import Base


class Attribute(CategoryRelationMixin, Base):
    @declared_attr
    def _category_back_populates(cls):
        return TbHelper.generate_tn(cls)

    _category_nullable = True  # For common products

    name: Mapped[str] = mapped_column(
        String(attr_helper.NAME_MAX_LEN),
        nullable=attr_helper.NAME_NULLABLE,
    )
    type: Mapped[str] = mapped_column(
        String(attr_helper.TYPE_STR_MAX_LEN),
        nullable=attr_helper.TYPE_STR_NULLABLE,
    )
