import pytest
from test_Simplefixture import api_url

def test_case1():
    print("Testcase 1 is executed")

def test_case2():
    print("Testcase 2 is executed")

def test_case3():
    print("Testcase 3 is executed")

def test_case4():
    print("Testcase 4 is executed")

def test_case5():
    print("Testcase 5 is executed")

def test_login():
    print("login Test is executed")


def test_api(api_url):
    assert "https" in api_url

''' for singletest  wise running --- pytest -k "test_login" -n 5 --html=report.html'''


'''  for paralell --- run ---- pytest test_paralell.py -n 3 -v'''


''' pytest .\Test_Parallel.py -n -3 --html=report.html'''

