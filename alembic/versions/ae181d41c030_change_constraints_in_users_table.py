"""Change constraints in users table

Revision ID: ae181d41c030
Revises: f55ecebb0113
Create Date: 2025-10-18 19:58:56.592521

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ae181d41c030"
down_revision: Union[str, Sequence[str], None] = "f55ecebb0113"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_unique_constraint("uq_users_email", "users", ["email"])

    op.alter_column(
        "users",
        "lastname",
        existing_type=sa.String(length=128),
        nullable=True,
    )


def downgrade():
    op.drop_constraint("uq_users_email", "users", type_="unique")

    op.alter_column(
        "users",
        "lastname",
        existing_type=sa.String(length=128),
        nullable=False,
    )
