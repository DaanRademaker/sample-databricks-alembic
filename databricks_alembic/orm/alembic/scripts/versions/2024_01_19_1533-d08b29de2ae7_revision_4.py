"""revision 4

Revision ID: d08b29de2ae7
Revises: 68c1ef671ef7
Create Date: 2024-01-19 15:33:15.818529

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d08b29de2ae7"
down_revision: Union[str, None] = "68c1ef671ef7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("test_model", sa.Column("some_added_column_non_nullable", sa.String(), nullable=True))
    op.execute("UPDATE test_model SET some_added_column_non_nullable = 'some_value'")
    op.alter_column("test_model", "some_added_column_non_nullable", nullable=False)


def downgrade() -> None:
    op.drop_column("test_model", "some_added_column_non_nullable")
