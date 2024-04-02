"""Tests for the project."""

from test_project_ci_cd import __version__, login
from test_project_ci_cd.calc import add


def test_version():
    """Test the version."""
    assert __version__ is not None


def test_login():
    """Test login function"""
    assert login(username="admin", password="admin1")


def test_add():
    """Test add function."""
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(1, 4) == 5
    assert add(1, 5) == 6
    assert add(1, 6) == 7
    assert add(1, 7) == 8
    assert add(1, 8) == 9
    assert add(1, 9) == 10
    assert add(1, 10) == 11
    assert add(1, 11) == 12
    assert add(1, 12) == 13
    assert add(1, 13) == 14
    assert add(1, 14) == 15
    assert add(1, 15) == 16
    assert add(1, 16) == 17
    assert add(1, 17) == 18
    assert add(1, 18) == 19
    assert add(1, 19) == 20
    assert add(1, 20) == 21
    assert add(1, 21) == 22
    assert add(1, 22) == 23
    assert add(1, 23) == 24
    assert add(1, 24) == 25
    assert add(1, 25) == 26
    assert add(1, 26) == 27
    assert add(1, 27) == 28
    assert add(1, 28) == 29
    assert add(1, 29) == 30
    assert add(1, 30) == 31
    assert add(1, 31) == 32
    assert add(1, 32) == 33
    assert add(1, 33) == 34
    assert add(1, 34) == 35
    assert add(1, 35) == 36
    assert add(1, 36) == 37
    assert add(1, 37) == 38
    assert add(1, 38) == 39
    assert add(1, 39) == 40
