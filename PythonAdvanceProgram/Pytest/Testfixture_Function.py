# scope is run before and after ever fun

import pytest

@pytest.fixture
def openbrowser():
    print("\nOpening browser")

@pytest.fixture
def closebrowser():
    print("\nClosing browser")

@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("Enter username")
    print("Enter password")
    print("Click login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("User logged out")


# fixtures at class level
# fixtures at module level
# fixtures at session level