import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (4, 5, 9),

    pytest.param(6, 7, 20, marks=pytest.mark.xfail(reason="Bug #101")),
    pytest.param(8, 2, 15, marks=pytest.mark.xfail(reason="Bug #102")),

    (10, 5, 15)
])
def test_add(a, b, result):
    assert a + b == result
