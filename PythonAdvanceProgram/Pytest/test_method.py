# runs before and after the test methods inside the class
#used inside the class

# incase of inheritance set up and teardown are considered

class Testclass:

    @classmethod
    def setup_class(cls):
        print("API Authorisation needed with username and password")

    @classmethod
    def teardown_class(cls):
        print("API Authorisation closed")

    def setup_method(method):
        print("Opening the browser")

    @classmethod
    def teardown_method(method):
        print("Closing the browser")

    def test_case1(self):
        print("Testcase 1 is executed")

    def test_case2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")


class Testclass2(Testclass):

    def test_case1(self):
        print("Testcase 1 is executed")

    def test_case2(self):
        print("Testcase 2 is executed")

    def test_case3(self):
        print("Testcase 3 is executed")


# To run this use this command pytest test_method.py -v -s --html=test_method_report.html
