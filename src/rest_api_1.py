"""
testing rest methods for url-1
"""
import json
import pytest
import requests

URL = 'https://dog.ceo/api/breeds/list/all'


@pytest.fixture()
def response():
    return requests.get(URL)


def json_data():
    return json.loads(requests.get(URL).content)


def test_len_content():
    assert len(requests.get(URL).content) is not None


def test_header(response):
    assert response.headers['Content-Type'] == 'application/json'


@pytest.mark.parametrize("breed, values",
                         [('bulldog', ['boston', 'english', 'french']), ('akita', [])])
def test_dogs_breed(breed, values):
    assert json_data()['message'][breed] == values


@pytest.mark.parametrize("array, length", [('message', 95), ('status', 7)])
def test_length(array, length):
    assert len(json_data()[array]) == length


@pytest.mark.parametrize("extra_raw, status_code", [(None, 200), ('ddd', 404)])
def test_response_code(extra_raw, status_code):
    if extra_raw is None:
        url_formed = URL
    else:
        url_formed = URL + str(extra_raw)
    response_new = requests.get(url_formed)
    assert response_new.status_code == status_code
