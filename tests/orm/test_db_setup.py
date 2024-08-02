from __future__ import annotations

from pytest_alembic.tests import (
    test_model_definitions_match_ddl as model_definitions_match_ddl,
)
from pytest_alembic.tests import (
    test_single_head_revision as single_head_revision,
)
from pytest_alembic.tests import (
    test_up_down_consistency as up_down_consistency,
)
from pytest_alembic.tests import (
    test_upgrade as upgrade,
)


def test_alembic_single_head_revision(alembic_runner, setup_alembic_test):
    """Assert that there only exists one head revision"""
    single_head_revision(alembic_runner)


def test_alembic_upgrade(alembic_runner):
    """Assert that the revision history can be run through from base to head."""
    upgrade(alembic_runner)


def test_alembic_up_down_consistency(alembic_runner):
    """Assert that all downgrades succeed. If an incompatible downgrade was added on purpose
    with the intention of preventing downgrades below a certain point, make sure to set the minimum
    downgrade revision in the conftest.py file."""
    up_down_consistency(alembic_runner)


def test_alembic_model_definitions_match_ddl(alembic_runner):
    """Assert that the state of the migrations matches the state of the models describing the DDL."""
    model_definitions_match_ddl(alembic_runner)
