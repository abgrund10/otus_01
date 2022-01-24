"""
testing rest methods for url-2
"""
import json

import pytest
import requests

URL = 'https://api.openbrewerydb.org/breweries?by_city=san_diego'


@pytest.fixture()
def response():
    return requests.get(URL)


def json_data():
    return json.loads(requests.get(URL).content)


def test_len_content():
    assert len(requests.get(URL).content) is not None
    assert len(json_data()) == 20


def test_header(response):
    assert response.headers['Content-Type'] != 'application/json'


@pytest.mark.parametrize("i, key, value", [(0, 'name', "10 Barrel Brewing Co"), (1, 'name', "2Kids Brewing Company")])
def test_json_content(i, key, value):
    assert json_data()[i][key] == value


@pytest.mark.parametrize("extra_raw, status_code", [(None, 200), ('ddd', 200)])
def test_response_code(extra_raw, status_code):
    if extra_raw is None:
        url_formed = URL
    else:
        url_formed = URL + str(extra_raw)
    response_new = requests.get(url_formed)
    assert response_new.status_code == status_code
