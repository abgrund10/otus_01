from urllib.error import URLError

import requests

def test_url(url, status_code):
    response = requests.get(url)
    assert r.status_code == int(status_code)
