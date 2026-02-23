# parameterisation testing multiple set of test data with the same fun
#@pytest.mark.parameterize()
#no parameters used

def test_add1():
    assert 2+3 == 5

def test_add2():
    assert 4+5 == 9

import pytest
@pytest.mark.parametrize("a, b , result", [
    (2,3,5),
    (4,5,9),
    (8,10,12)
])

def test_add(a,b,result):
    assert a+b == result


''' run --- pytest test_parameterisation.py -v -s --html=test_parameter.html'''

#single parameter
@pytest.mark.parametrize("number",[1,2,3,4,5])
def test_even(number):
    assert number%2 == 0