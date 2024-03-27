"""Test package for CI/CD."""

__version__ = "0.1.0"

session = None


def login(username: str, password: str):
    """Test login function."""
    global session
    if username == "admin" and password == "admin1":
        session = "admin"
        return True
    else:
        return False


def logout():
    """Logout function."""
    global session
    try:
        if not session:
            raise Exception("No session found")
        session = None
    except:
        print("No session found")
