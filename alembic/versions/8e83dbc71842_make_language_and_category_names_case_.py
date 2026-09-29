"""make language and category names case insensitive unique

Revision ID: 8e83dbc71842
Revises: 5f86365571eb
Create Date: 2026-09-24 17:02:14.086041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e83dbc71842'
down_revision: Union[str, Sequence[str], None] = '5f86365571eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "uq_language_name_lower",
        "language",
        [sa.text("lower(name)")],
        unique=True,
    )
    op.create_index(
        "uq_url_category_name_lower",
        "url_category",
        [sa.text("lower(name)")],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("uq_url_category_name_lower", table_name="url_category")
    op.drop_index("uq_language_name_lower", table_name="language")