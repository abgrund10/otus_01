import pytest
from selenium import webdriver
import requests


@pytest.fixture(scope="session")
def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='http://www.opencart.com')
    parser.addoption('--browser', action='store', default='Chrome')
    parser.addoption('--way_to_execute', action='store', default='localhost')


@pytest.fixture
def url(request):
    with allure.step(f'POST request to:'):
        return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(url, browser, request, way_to_execute):
    runner = request.config.getoption("--way_to_execute")
    if runner == 'localhost':
        url_final = url + ':4444/wd/hub'
    else:
        url_final = url
    caps = {
            "browserName": browser,
            "screenResolution": "1280x1024",
            "name": "agr tests",
            "selenoid:options": {
                "sessionTimeout": "60s"
            },
            # 'goog:chromeOptions': {}
        }

    wd = webdriver.Remote(
        command_executor=url_final,
        desired_capabilities=caps)
    return wd


@pytest.fixture
def test_teardown(driver, url):
    driver.quit()
