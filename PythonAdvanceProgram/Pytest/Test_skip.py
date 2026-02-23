# skip - if defects are there
# skip - if testcases are absolute
# when the features are partially implemented

import pytest

def test_case1():
    print("Testcase 1 is executed")

@pytest.mark.skip
def test_case2():
    print("Testcase 2 is executed")

def test_case3():
    print("Testcase 3 is executed")

def test_case4():
    print("Testcase 4 is executed")
# this is not in format of pytest as it shld start with test
def openbrowser():
    print("Opening the browser")




