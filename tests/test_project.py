"""Tests for the project."""

from test_project_ci_cd import __version__


def test_all():
    """Test the version."""
    assert __version__ is not None
