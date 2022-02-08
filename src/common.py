"""
common elements
"""
import requests
import json
from cerberus import Validator



def json_data_common(URL):
    return json.loads(requests.get(URL).content)

def test_len_content_common(URL):
    assert len(requests.get(URL).content) is not None


def test_response_code_common(URL, extra_raw, status_code):
    if extra_raw is None:
        url_formed = URL
    else:
        url_formed = URL + str(extra_raw)
    response_new = requests.get(url_formed)
    assert response_new.status_code == status_code


def test_validate_cerber_common(URL, schema1):
    def json_data_common(URL):
        return json.loads(requests.get(URL).content)
    schema_validator = Validator(schema1)
    is_valid = schema_validator.validate(json_data_common(URL))
    assert is_valid, "No errors should be detected for valid object"