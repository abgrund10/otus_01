"""
testing rest methods for url-1
"""
import pytest
import requests
import common

class Testdata:

    @pytest.fixture()
    def response(self):
        return requests.get(URL)

    def test_header(self, response):
        assert response.headers['Content-Type'] == 'application/json'


    def test_validation2(self):
        common.test_validate_cerber_common(URL, schema1)


    #@pytest.mark.smoke
    @pytest.mark.parametrize("breed, values",
                             [('bulldog', ['boston', 'english', 'french']), ('akita', [])])
    def test_dogs_breed(self, breed, values):
            assert common.json_data_common(URL)['message'][breed] == values


    #@pytest.mark.smoke
    @pytest.mark.parametrize("array, length", [('message', 95), ('status', 7)])
    def test_length(array, length):
        assert len(common.json_data_common(URL)[array]) == length


URL = 'https://dog.ceo/api/breeds/list/all'

schema1 = {
    "message": {'type': ['dict', 'list']},
    "status": {'type': 'string'},
}
