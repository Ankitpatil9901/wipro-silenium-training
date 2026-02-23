#fixture dependency - the 2nd fixture will work onl when first fixture gets exeuted

import pytest

def test(fixture_b):
    assert fixture_b == "Data from A + form B"