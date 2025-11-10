"""Make category name unique in categories table

Revision ID: 427b9cbc5a68
Revises: 5ace262e331e
Create Date: 2025-11-10 14:02:03.613928

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "427b9cbc5a68"
down_revision: Union[str, Sequence[str], None] = "5ace262e331e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        "idx_unique_categories_name",
        "categories",
        ["name"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "idx_unique_categories_name",
        "categories",
        type_="unique",
    )
    # ### end Alembic commands ###
