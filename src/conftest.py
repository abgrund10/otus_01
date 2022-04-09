import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='https://www.opencart.com/')
    parser.addoption('--browser', action='store', default='Chrome')


@pytest.fixture(scope="module")
def url(request):
    with allure.step(f'POST request to:'):
        return request.config.getoption("--url")


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def driver(url, browser):
    driver = eval("webdriver.{browser}()".format(browser=browser.title()))
    driver.get(url)

@pytest.fixture(scope="module")
def test_teardown(driver, url):
    driver.quit()
