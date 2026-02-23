
#1.Write a test that is skipped because a feature is not implemented yet.
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment_feature():
    assert False



