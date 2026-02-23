# grouping - set of testcases run together - issues fix i that module

import pytest

def test_case1(self):
    print("Testcase 1 is executed")

@pytest.mark.sanity
def test_case2(self):
    print("Testcase 2 is executed")

@pytest.mark.sanity
@pytest.mark.regression
def test_case3(self):
    print("Testcase 3 is executed")

''' run pytest -m "regression and sanity" -v -s  --html=test_group.html'''