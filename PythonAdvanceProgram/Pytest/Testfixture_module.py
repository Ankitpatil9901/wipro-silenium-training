#scope - module - runs per file


import pytest

@pytest.mark.usefixtures("setupapi")
def test_one():
    print("TestCase1")

def test_two():
    print("TestCase2")


