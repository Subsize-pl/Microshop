"""add discount_count column to products table

Revision ID: 2f133b92baf8
Revises: e32d9c1700a7
Create Date: 2025-10-16 19:45:45.984833

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import core

# revision identifiers, used by Alembic.
revision: str = "2f133b92baf8"
down_revision: Union[str, Sequence[str], None] = "e32d9c1700a7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "discount_price",
            sa.Integer(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("products", "discount_price")
