import sqlalchemy as sa
from databricks.sqlalchemy import TIMESTAMP

from databricks_alembic.orm.models import Base


class TestModel(Base):
    """
    Table containing observations information
    """

    __tablename__ = "test_model"
    __application_name__ = "some_application"
    bigint_col = sa.Column(sa.BigInteger, primary_key=True)
    string_col = sa.Column(sa.String)
    tinyint_col = sa.Column(sa.SmallInteger())
    int_col = sa.Column(sa.String)
    numeric_col = sa.Column(sa.Numeric(10, 2))
    boolean_col = sa.Column(sa.Boolean)
    date_col = sa.Column(sa.Date)
    datetime_col = sa.Column(TIMESTAMP)
    datetime_col_ntz = sa.Column(sa.DateTime)
    time_col = sa.Column(sa.Time)
    uuid_col = sa.Column(sa.Uuid)
    some_added_column = sa.Column(sa.String, nullable=True)
    some_added_column_non_nullable = sa.Column(sa.String, nullable=False)
