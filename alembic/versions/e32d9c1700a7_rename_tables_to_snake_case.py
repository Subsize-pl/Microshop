"""rename tables to snake case

Revision ID: e32d9c1700a7
Revises: bcfd110646f4
Create Date: 2025-10-16 19:39:39.348063

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e32d9c1700a7"
down_revision: Union[str, Sequence[str], None] = "bcfd110646f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("cartitems", "cart_items")
    op.rename_table("orderitems", "order_items")
    op.rename_table("productattributes", "product_attributes")


def downgrade() -> None:
    """Downgrade schema: revert table names to original."""
    op.rename_table("cart_items", "cartitems")
    op.rename_table("order_items", "orderitems")
    op.rename_table("product_attributes", "productattributes")
