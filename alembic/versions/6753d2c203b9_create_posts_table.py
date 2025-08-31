"""create posts table

Revision ID: 6753d2c203b9
Revises: 
Create Date: 2025-07-17 23:49:08.404291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6753d2c203b9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("description", sa.String()))


def downgrade():
    op.drop_column("posts", "description")
