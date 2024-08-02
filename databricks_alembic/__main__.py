import typer

from databricks_alembic.orm.cli import orm_cli

main_cli = typer.Typer()

main_cli.add_typer(orm_cli, name="orm")


def main():
    main_cli()


if __name__ == "__main__":
    main()
