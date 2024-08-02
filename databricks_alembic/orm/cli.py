import os
from typing import Annotated, Optional

import typer

from databricks_alembic.orm.db_setup import downgrade_to_revision, run_migrations

tables = typer.Typer(help="Commands for all tables")
orm_cli = typer.Typer(help="Sqlalchemy commands")
orm_cli.add_typer(tables, name="tables")


def get_sa_url() -> str:
    host = os.getenv("DATABRICKS_SERVER_HOSTNAME")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    access_token = os.getenv("DATABRICKS_TOKEN")
    catalog = os.getenv("DATABRICKS_CATALOG")
    schema = os.getenv("DATABRICKS_SCHEMA")
    return f"databricks://token:{access_token}@{host}?http_path={http_path}&catalog={catalog}&schema={schema}"


@tables.command()
def upgrade(sa_url: Annotated[Optional[str], typer.Option(help="SQL alchemy url to databricks host")] = None):
    if not sa_url:
        sa_url = get_sa_url()

    run_migrations(sa_url)


@tables.command()
def downgrade(
    revision: Annotated[str, typer.Option(help="revision id to downgrade to")],
    sa_url: Annotated[Optional[str], typer.Option(help="SQL alchemy url to databricks host")] = None,
):
    if not sa_url:
        sa_url = get_sa_url()

    downgrade_to_revision(sa_url, revision=revision)
