from typing import Union, Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8cd634fc4d84"
down_revision: Union[str, Sequence[str], None] = "427b9cbc5a68"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add enum
    category_status = sa.Enum("active", "inactive", name="category_status")
    category_status.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "categories",
        sa.Column(
            "status",
            category_status,
            server_default="active",
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_column("categories", "status")

    # Remove enum
    category_status = sa.Enum("active", "inactive", name="category_status")
    category_status.drop(op.get_bind(), checkfirst=True)
