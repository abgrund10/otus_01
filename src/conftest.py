from datetime import datetime
import pytest
import logging
from selenium import webdriver

url = "https://nasport.fun/"


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(request):
    logger = logging.getLogger('driver')
    driver.test_name = request.node.name
    logger.addHandler(logging.FileHandler(driver.test_name))
    logger.info(f"{logger.name} ===> Test {driver.test_name} started at {datetime.now()}")
    driver.log_level = "INFO"
    driver.log_path = f"logs/{driver.test_name}_{datetime.now()}.log"
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        wd = webdriver.Chrome()
    elif browser == "firefox":
        wd = webdriver.Firefox()
    elif browser == "opera":
        wd = webdriver.Opera()
    else:
        raise Exception("Unknown browser. Please select from following list: chrome, firefox, opera")
    wd.get(url)

    return wd
