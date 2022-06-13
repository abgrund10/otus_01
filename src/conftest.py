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


@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        webdriver.Chrome().get(url)
    elif browser == "firefox":
        webdriver.Firefox().get(url)
    elif browser == "opera":
        webdriver.Opera().get(url)
    else:
        raise Exception("Browser not found")


@pytest.fixture
def test_teardown(driver):
    driver.quit()
