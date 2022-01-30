import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='https://www.opencart.com/')
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")