#3.Write a test that checks an API health endpoint.If status code is not 200 → skip the test dynamically.
import pytest
import requests

def test_api_health():
    response = requests.get("https://example.com/health")

    if response.status_code != 200:
        pytest.skip(f"API not healthy. Status code: {response.status_code}")

    assert response.status_code == 200

