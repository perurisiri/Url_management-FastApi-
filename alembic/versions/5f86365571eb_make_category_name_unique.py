"""make category name unique

Revision ID: 5f86365571eb
Revises: 13d26057105c
Create Date: 2026-09-24 16:54:50.372126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f86365571eb'
down_revision: Union[str, Sequence[str], None] = '13d26057105c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("uq_url_category_name", "url_category", ["name"])


def downgrade() -> None:
    op.drop_constraint("uq_url_category_name", "url_category", type_="unique")