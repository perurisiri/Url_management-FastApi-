"""add unique constraints to language name and code

Revision ID: 13d26057105c
Revises: 
Create Date: 2026-09-24 16:28:15.960744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13d26057105c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("uq_language_name", "language", ["name"])
    op.create_unique_constraint("uq_language_code", "language", ["code"])


def downgrade() -> None:
    op.drop_constraint("uq_language_code", "language", type_="unique")
    op.drop_constraint("uq_language_name", "language", type_="unique")