#function level setup and tear down
#these run before and after each test function

def setup_function(function):
    print("Opening the browser")

def teardown_function(function):
    print("Closing the browser")


def test_case1():
    print("Testcase 1 is executed")

def test_case2():
    print("Testcase 2 is executed")

def test_case3():
    print("Testcase 3 is executed")

