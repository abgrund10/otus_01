import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='http://www.opencart.com')
    parser.addoption('--browser', action='store', default='Chrome')
    parser.addoption('--way_to_execute', action='store', default='localhost')


@pytest.fixture(scope="module")
def url(request):
    with allure.step(f'POST request to:'):
        return request.config.getoption("--url")


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def driver(url, browser, way_to_execute):
    if way_to_execute == 'localhost':
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

@pytest.fixture(scope="module")
def test_teardown(driver, url):
    driver.quit()
