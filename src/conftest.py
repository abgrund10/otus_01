from datetime import datetime
import pytest
import logging
from selenium import webdriver

url = "https://nasport.fun/"


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    logger = logging.getLogger('driver')
    driver.test_name = request.node.name
    logger.addHandler(logging.FileHandler(driver.test_name))
    logger.info(f"{logger.name} ===> Test {driver.test_name} started at {datetime.now()}")
    driver.log_level = "INFO"
    driver.log_path = f"logs/{driver.test_name}_{datetime.now()}.log"
    return request.config.getoption("--browser")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        wd = webdriver.Chrome().get(url)
    elif browser == "firefox":
        wd = webdriver.Firefox().get(url)
    elif browser == "opera":
        wd = webdriver.Opera().get(url)
    else:
        raise Exception("Unknown browser. Please select from following list: chrome, firefox, opera")

    return wd
