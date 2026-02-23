

import pytest


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("Click the logintbtn")

    def test_logout(self):
        print("user is logout")
