import argparse

import requests
import pytest


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def test_url():
    response_new = requests.get(url())
    st_code = response_new.status_code
    assert status_code == st_code
