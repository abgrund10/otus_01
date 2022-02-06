import pytest
import requests


@pytest.mark.smoke
def test_url(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code)