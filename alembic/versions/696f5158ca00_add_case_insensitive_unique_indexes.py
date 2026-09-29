"""add case insensitive unique indexes

Revision ID: 696f5158ca00
Revises: 38604b377521
Create Date: 2026-09-27 15:19:34.587559

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '696f5158ca00'
down_revision: Union[str, Sequence[str], None] = '38604b377521'
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
    op.drop_index(
        "uq_url_category_name_lower",
        table_name="url_category"
    )

    op.drop_index(
        "uq_language_name_lower",
        table_name="language"
    )
