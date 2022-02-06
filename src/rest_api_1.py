"""
testing rest methods for url-1
"""
import json
import pytest
import requests
from cerberus import Validator

URL = 'https://dog.ceo/api/breeds/list/all'

schema1 = {
    "message": {'type': ['dict', 'list']},
    "status": {'type': 'string'},
}


@pytest.fixture()
def response():
    return requests.get(URL)


def test_header(response):
    assert response.headers['Content-Type'] == 'application/json'


#@pytest.mark.smoke
@pytest.mark.parametrize("breed, values",
                         [('bulldog', ['boston', 'english', 'french']), ('akita', [])])
def test_validate_cerber_common(schema1):
    def test_dogs_breed(breed, values):
        assert json_data()['message'][breed] == values
    return test_dogs_breed


#@pytest.mark.smoke
@pytest.mark.parametrize("array, length", [('message', 95), ('status', 7)])
def test_length(array, length):
    assert len(json_data()[array]) == length



# february updates
#@pytest.mark.validation
def test_validate_cerber(schema):
    schema_validator = Validator(schema)
    is_valid = schema_validator.validate(json_data())
    print(schema_validator.errors)
    assert is_valid, "No errors should be detected for valid object"
