import os
from pathlib import Path
from uuid import uuid4

import pytest
from databricks.sdk import WorkspaceClient
from pytest_alembic.config import Config

DATABRICKS_TOKEN = os.environ["DATABRICKS_TOKEN"]
DATABRICKS_SERVER_HOSTNAME = os.environ["DATABRICKS_SERVER_HOSTNAME"]
DATABRICKS_SERVER_PORT = os.environ["DATABRICKS_SERVER_PORT"]
DATABRICKS_CATALOG = os.environ["DATABRICKS_CATALOG"]
DATABRICKS_ALEMBIC_TEST_CATALOG = os.environ["DATABRICKS_ALEMBIC_TEST_CATALOG"]
DATABRICKS_HTTP_PATH = os.environ["DATABRICKS_HTTP_PATH"]


def alembic_sa_url(schema_name: str) -> str:
    databricks_sql_warehouse_http_path = DATABRICKS_HTTP_PATH
    return (
        f"databricks://token:{DATABRICKS_TOKEN}@{DATABRICKS_SERVER_HOSTNAME}?http_path="
        f"{databricks_sql_warehouse_http_path}&catalog={DATABRICKS_ALEMBIC_TEST_CATALOG}&schema={schema_name}"
    )


@pytest.fixture()
def setup_alembic_test():
    """This fixture should create a schema in databricks
    with some uuid and return the schema name.
    """
    schema_name = str(uuid4())
    client = WorkspaceClient(host=DATABRICKS_SERVER_HOSTNAME, token=DATABRICKS_TOKEN)
    client.schemas.create(name=schema_name, catalog_name="alembic_tests", comment="created for alembic tests run")
    os.environ["ALEMBIC_SA_URL"] = alembic_sa_url(schema_name)
    # Create databricks schema
    yield schema_name

    # During teardown clean up the schema
    tables = list(client.tables.list(catalog_name="alembic_tests", schema_name=schema_name))
    for table in tables:
        client.tables.delete(
            full_name=f"alembic_tests.{schema_name}.{table.name}",
        )

    client.schemas.delete(full_name=f"alembic_tests.{schema_name}")


@pytest.fixture()
def alembic_config(setup_alembic_test) -> Config:
    """Override this fixture to configure the exact alembic context setup required."""
    return Config(
        {
            "file": os.path.join(
                Path(__file__).parent.parent.parent,
                "sample_databricks_alembic/orm/alembic/alembic.ini",
            ),
            "script_location": os.path.join(
                Path(__file__).parent.parent.parent,
                "sample_databricks_alembic/orm/alembic/scripts",
            ),
            "sqlalchemy.url": alembic_sa_url(setup_alembic_test),
        },
    )
