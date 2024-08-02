"""revision 2

Revision ID: 48ffcc7ba93e
Revises: b37e86d5acf7
Create Date: 2024-01-19 14:41:09.490428

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "48ffcc7ba93e"
down_revision: Union[str, None] = "b37e86d5acf7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("ALTER TABLE test_model SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name')")
    op.execute("ALTER TABLE test_model ADD COLUMN new_column string")
    op.execute("UPDATE test_model SET new_column = int_col")
    op.execute("ALTER TABLE test_model DROP COLUMN int_col")
    op.execute("ALTER TABLE test_model RENAME COLUMN new_column TO int_col")


def downgrade():
    op.execute("ALTER TABLE test_model SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name')")
    op.execute("ALTER TABLE test_model ADD COLUMN new_column integer")
    op.execute("UPDATE test_model SET new_column = int_col")
    op.execute("ALTER TABLE test_model DROP COLUMN int_col")
    op.execute("ALTER TABLE test_model RENAME COLUMN new_column TO int_col")
