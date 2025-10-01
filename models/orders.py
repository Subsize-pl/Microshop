from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from core.mixins import TimestampMixin, UserRelationMixin
from models import Base
from core.helpers import TbHelper


class OrderStatus(Enum):
    pending = "pending"  # Неоплачено
    paid = "paid"  # Оплачено
    awaiting = "awaiting"  # В ожидании отправки
    shipped = "shipped"  # Отправлен
    delivering = "delivering"  # Доставляется
    delivered = "delivered"  # Доставлено
    cancelled = "cancelled"  # Отменён


class Order(UserRelationMixin, TimestampMixin, Base):
    @declared_attr
    def _user_back_populates(cls):
        return TbHelper.generate_tn(cls)

    status: Mapped[OrderStatus] = mapped_column(
        SQLEnum(OrderStatus, name="order_status"),
        nullable=False,
        default=OrderStatus.pending,
        server_default=OrderStatus.pending.value,
    )
