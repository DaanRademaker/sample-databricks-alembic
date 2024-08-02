import os
from pathlib import Path

from alembic import command
from alembic.config import Config


def run_migrations(dsn: str, revision: str | None = None):
    if not revision:
        revision = "head"
    alembic_cfg = Config()
    script_location = os.path.join(Path(__file__).parent, "alembic/scripts")
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", dsn)
    command.upgrade(alembic_cfg, revision)


def downgrade_to_revision(dsn: str, revision: str):
    alembic_cfg = Config()
    script_location = os.path.join(Path(__file__).parent, "alembic/scripts")
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", dsn)
    command.downgrade(alembic_cfg, revision)
