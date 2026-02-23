
#2.write a test that runs only on Linux and skips on Windows.

import pytest
import sys

@pytest.mark.skipif(sys.platform.startswith("win"),
                    reason="This test runs only on Linux")
def test_linux_feature():
    assert True


