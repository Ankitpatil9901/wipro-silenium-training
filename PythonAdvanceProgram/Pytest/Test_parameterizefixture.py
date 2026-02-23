import pytest
@pytest.fixture(params= ["chrome","brave"])
#request - pytest object that contains information about who is calling the fixture and with that data
def browser(request):
        print("Invoke chrome browser",request.param)
        return request.param

def test_browser(browser):
        assert browser in ["chrome" , "brave"]



# selecting even or odd number


import pytest

@pytest.fixture(params=[2, 5, 8, 11])
def number(request):
    return request.param

def test_even_number(number):
    assert number % 2 == 0



