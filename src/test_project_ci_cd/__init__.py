"""Test package for CI/CD."""

__version__ = "0.1.0"


def login(username: str, password: str):
    """Test login function."""
    return username == "admin" and password == "admin1"
