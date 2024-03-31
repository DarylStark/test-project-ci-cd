"""Tests for the project."""

from test_project_ci_cd import __version__, login


def test_version():
    """Test the version."""
    assert __version__ is not None


def test_login():
    """Test login function"""
    assert login(username="admin", password="admin1")
