"""Test package for CI/CD.

Contains only testcode.
"""

__version__ = "0.1.0"

session = None


class TPException(Exception):
    """Custom exception for test project."""


def login(username: str, password: str):
    """Test login function."""
    global session
    if username == "admin" and password == "admin1":
        session = "admin"
        return True
    return False


def logout():
    """Logout function."""
    global session
    try:
        if not session:
            raise TPException("No session found")
        session = None
    except TPException:
        print("No session found")
