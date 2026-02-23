#4.Mark a failing test as xfail with reason: "Bug #123".
import pytest

@pytest.mark.xfail(reason="Bug #123")
def test_login_with_invalid_password():
    assert 1 == 2