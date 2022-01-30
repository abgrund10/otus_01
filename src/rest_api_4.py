from urllib.error import URLError

import requests

def test_url(url, status_code):
    response = requests.get(url)

    try:
        assert int(status_code) == 200
        assert response.status_code == 200

    except URLError:
        assert int(status_code) == 404
        assert response.status_code == 404