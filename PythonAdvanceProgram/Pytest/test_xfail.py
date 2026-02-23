# xfail is a marker used to indicate that a test is expected to fail due to a known issue

import pytest
@pytest.mark.xfail(reason = "known bug in the third part library ")
def test_function():
    assert (1+1) == 3
@pytest.mark.sanity
def test_case1():
    print("Testcase 1 is executed")
@pytest.mark.regression
def test_case2():
    print("Testcase 2 is executed")
@pytest.mark.db
def test_case3():
    print("Testcase 3 is executed")