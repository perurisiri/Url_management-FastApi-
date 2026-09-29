"""add category case insensitive unique index

Revision ID: 38604b377521
Revises: 8e83dbc71842
Create Date: 2026-09-27 14:48:35.438332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38604b377521'
down_revision: Union[str, Sequence[str], None] = '8e83dbc71842'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "uq_url_category_name_lower",
        "url_category",
        [sa.text("lower(name)")],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(
        "uq_url_category_name_lower",
        table_name="url_category",
    )