"""Tests for the project."""

from test_project_ci_cd import __version__, login
from test_project_ci_cd.calc import get_diff, get_product, get_quotient, get_sum


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


def test_product():
    """Test product function."""
    assert get_product(1, 2) == 2
    assert get_product(1, 3) == 3
    assert get_product(1, 4) == 4
    assert get_product(1, 5) == 5
    assert get_product(1, 6) == 6
    assert get_product(1, 7) == 7
    assert get_product(1, 8) == 8
    assert get_product(1, 9) == 9
    assert get_product(1, 10) == 10
    assert get_product(1, 11) == 11
    assert get_product(1, 12) == 12
    assert get_product(1, 13) == 13
    assert get_product(1, 14) == 14
    assert get_product(1, 15) == 15
    assert get_product(1, 16) == 16
    assert get_product(1, 17) == 17
    assert get_product(1, 18) == 18
    assert get_product(1, 19) == 19
    assert get_product(1, 20) == 20
    assert get_product(1, 21) == 21
    assert get_product(1, 22) == 22
    assert get_product(1, 23) == 23
    assert get_product(1, 24) == 24
    assert get_product(1, 25) == 25
    assert get_product(1, 26) == 26
    assert get_product(1, 27) == 27
    assert get_product(1, 28) == 28
    assert get_product(1, 29) == 29
    assert get_product(1, 30) == 30
    assert get_product(1, 31) == 31
    assert get_product(1, 32) == 32
    assert get_product(1, 33) == 33
    assert get_product(1, 34) == 34
    assert get_product(1, 35) == 35
    assert get_product(1, 36) == 36


def test_quotient():
    """Test quotient function."""
    assert get_quotient(1, 2) == 0.5
    assert get_quotient(1, 3) == 0.3333333333333333
    assert get_quotient(1, 4) == 0.25
    assert get_quotient(1, 5) == 0.2
    assert get_quotient(1, 6) == 0.16666666666666666
    assert get_quotient(1, 7) == 0.14285714285714285
    assert get_quotient(1, 8) == 0.125
    assert get_quotient(1, 9) == 0.1111111111111111
    assert get_quotient(1, 10) == 0.1
    assert get_quotient(1, 11) == 0.09090909090909091
    assert get_quotient(1, 12) == 0.08333333333333333
    assert get_quotient(1, 13) == 0.07692307692307693
    assert get_quotient(1, 14) == 0.07142857142857142
    assert get_quotient(1, 15) == 0.06666666666666667
    assert get_quotient(1, 16) == 0.0625
    assert get_quotient(1, 17) == 0.058823529411764705
    assert get_quotient(1, 18) == 0.05555555555555555
    assert get_quotient(1, 19) == 0.05263157894736842
    assert get_quotient(1, 20) == 0.05
    assert get_quotient(1, 21) == 0.047619047619047616
    assert get_quotient(1, 22) == 0.045454545454545456
    assert get_quotient(1, 23) == 0.043478260869565216


def test_diff():
    """Test difference function."""
    assert get_diff(1, 2) == -1
    assert get_diff(1, 3) == -2
    assert get_diff(1, 4) == -3
    assert get_diff(1, 5) == -4
    assert get_diff(1, 6) == -5
    assert get_diff(1, 7) == -6
    assert get_diff(1, 8) == -7
    assert get_diff(1, 9) == -8
    assert get_diff(1, 10) == -9
    assert get_diff(1, 11) == -10
    assert get_diff(1, 12) == -11
    assert get_diff(1, 13) == -12
    assert get_diff(1, 14) == -13
    assert get_diff(1, 15) == -14
    assert get_diff(1, 16) == -15
    assert get_diff(1, 17) == -16
    assert get_diff(1, 18) == -17
    assert get_diff(1, 19) == -18
    assert get_diff(1, 20) == -19
    assert get_diff(1, 21) == -20
    assert get_diff(1, 22) == -21
    assert get_diff(1, 23) == -22
    assert get_diff(1, 24) == -23
    assert get_diff(1, 25) == -24
    assert get_diff(1, 26) == -25
    assert get_diff(1, 27) == -26
    assert get_diff(1, 28) == -27
    assert get_diff(1, 29) == -28
    assert get_diff(1, 30) == -29
    assert get_diff(1, 31) == -30
    assert get_diff(1, 32) == -31
    assert get_diff(1, 33) == -32
    assert get_diff(1, 34) == -33
    assert get_diff(1, 35) == -34
    assert get_diff(1, 36) == -35
