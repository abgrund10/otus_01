from datetime import datetime

import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='"https://nasport.fun/"')
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--browser_version', action='store', default='101.0')


@pytest.fixture(scope='session')
def url(request):
    with allure.step(f'POST request to:'):
        return request.config.getoption("--url")


@pytest.fixture(scope='session')
def browser(request):
    logger = logging.getLogger('driver')
    driver.test_name = request.node.name
    logger.addHandler(logging.FileHandler(driver.test_name))
    logger.info(f"{logger.name} ===> Test {driver.test_name} started at {datetime.now()}")
    driver.log_level = "INFO"
    driver.log_path = f"logs/{driver.test_name}_{datetime.now()}.log"
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption("--browser")
    browserversion = request.config.getoption("--browser_version")
    url_final = url
    if browser == "chrome":
        options = Options()
        options.add_argument(browserversion)
        wd = webdriver.Chrome(options=options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument(browserversion)
        wd = webdriver.Firefox(options=firefox_options)
    elif browser == "opera":
        wd = webdriver.Opera()
    else:
        raise Exception("Unknown browser. Please select from following list: chrome, firefox, opera")

    return wd.get(url_final)


@pytest.fixture(scope='session')
def test_teardown(driver, url):
    driver.quit()
