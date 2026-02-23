# Used inside the class
# It will run

class Testclass:

    @classmethod
    def setup_class(cls):
        print("API Authorisation needed with username and password")

    @classmethod
    def teardown_class(cls):
        print("API Authorisation closed")

    def test_case1(self):
        print("Testcase 1 is executed")

    def test_case2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")


class Testclass2:

    def test_case1(self):
        print("Testcase 1 is executed")

    def test_case2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")
