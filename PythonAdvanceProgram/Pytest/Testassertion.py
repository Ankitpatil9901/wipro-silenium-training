#basic assertion -
#hard assertion - it will stop th execution of the test cases
# soft assertion - it will continue to run even if the assertion fails
from pytest_check import check


def test_add():
    result = 2+3
    assert result ==5

def test_boolean():
    assert True
    assert not False

# none value

def test_none():
    value = None
    assert value is None

# list assertion
def test_list():
    fruits =  ["apple","orange","banana"]
    assert "orange" in fruits

def test_dict():
    creds = {"username": "admin", "password":"123"}
    assert creds["password"]== "123"

# comparring list
def test_comparelist():
    assert [1,2,3] == [1,2,3]

# assertion with custom messages

def test_custom():
    result = 10
    assert result == 10, "Result should 5"


# soft assertion

def test_multiple():
    check.equal(1,2)
    check.equal(3,3)



