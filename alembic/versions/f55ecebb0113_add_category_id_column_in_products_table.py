"""Add category_id column in products table

Revision ID: f55ecebb0113
Revises: 2f133b92baf8
Create Date: 2025-10-16 20:26:21.391690

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f55ecebb0113"
down_revision: Union[str, Sequence[str], None] = "2f133b92baf8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column(
            "category_id", sa.Integer, sa.ForeignKey("categories.id"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_column("products", "category_id")
