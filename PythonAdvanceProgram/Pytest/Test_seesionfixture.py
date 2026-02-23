#session -- runs once for the entire pytest run

import pytest

@pytest.fixture(scope= "session")
def sessionsetup():
    print("Sessionsetup")
    yield
    print("sessionsetup")