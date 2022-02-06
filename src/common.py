"""
common elements
"""
import requests
import json
from cerberus import Validator


URL = ""

def json_data_common():
    return json.loads(requests.get(URL).content)


def test_len_content_common():
    assert len(requests.get(URL).content) is not None


def test_response_code_common(extra_raw, status_code):
    if extra_raw is None:
        url_formed = URL
    else:
        url_formed = URL + str(extra_raw)
    response_new = requests.get(url_formed)
    assert response_new.status_code == status_code


def test_validate_cerber_common(schema1):
    schema_validator = Validator(schema1)
    is_valid = schema_validator.validate(json_data_common())
    print(schema_validator.errors)
    assert is_valid, "No errors should be detected for valid object"