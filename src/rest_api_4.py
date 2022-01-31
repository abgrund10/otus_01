from urllib.error import URLError

import requests

def test_url(url, status_code):
    response = requests.get(url)

    try:
        assert r.status_code == int(status_code)

    except URLError:
        assert int(status_code) == 404
        assert response.status_code == 404
