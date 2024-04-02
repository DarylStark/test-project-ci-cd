"""Tests for the project."""

from test_project_ci_cd import __version__, login
from test_project_ci_cd.calc import get_sum


def test_version():
    """Test the version."""
    assert __version__ is not None


def test_login():
    """Test login function"""
    assert login(username="admin", password="admin1")


def test_add():
    """Test add function."""
    assert get_sum(1, 2) == 3
    assert get_sum(1, 3) == 4
    assert get_sum(1, 4) == 5
    assert get_sum(1, 5) == 6
    assert get_sum(1, 6) == 7
    assert get_sum(1, 7) == 8
    assert get_sum(1, 8) == 9
    assert get_sum(1, 9) == 10
    assert get_sum(1, 10) == 11
    assert get_sum(1, 11) == 12
    assert get_sum(1, 12) == 13
    assert get_sum(1, 13) == 14
    assert get_sum(1, 14) == 15
    assert get_sum(1, 15) == 16
    assert get_sum(1, 16) == 17
    assert get_sum(1, 17) == 18
    assert get_sum(1, 18) == 19
    assert get_sum(1, 19) == 20
    assert get_sum(1, 20) == 21
    assert get_sum(1, 21) == 22
    assert get_sum(1, 22) == 23
    assert get_sum(1, 23) == 24
    assert get_sum(1, 24) == 25
    assert get_sum(1, 25) == 26
    assert get_sum(1, 26) == 27
    assert get_sum(1, 27) == 28
    assert get_sum(1, 28) == 29
    assert get_sum(1, 29) == 30
    assert get_sum(1, 30) == 31
    assert get_sum(1, 31) == 32
    assert get_sum(1, 32) == 33
    assert get_sum(1, 33) == 34
    assert get_sum(1, 34) == 35
    assert get_sum(1, 35) == 36
    assert get_sum(1, 36) == 37
    assert get_sum(1, 37) == 38
    assert get_sum(1, 38) == 39
    assert get_sum(1, 39) == 40
