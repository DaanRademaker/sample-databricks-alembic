"""revision 3

Revision ID: 68c1ef671ef7
Revises: 48ffcc7ba93e
Create Date: 2024-01-19 15:16:38.589613

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "68c1ef671ef7"
down_revision: Union[str, None] = "48ffcc7ba93e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("test_model", sa.Column("some_added_column", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("test_model", "some_added_column")
