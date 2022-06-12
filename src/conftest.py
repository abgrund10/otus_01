from datetime import datetime
import pytest
import logging
from selenium import webdriver


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
    runner = request.config.getoption("--way_to_execute")
    browser = request.config.getoption("--browser")
    if runner == 'localhost':
        url_final = "http://localhost:4444/wd/hub"
        if browser == "chrome":
            wd = webdriver.Chrome().get(url_final)
        elif browser == "firefox":
            wd = webdriver.Firefox().get(url_final)
        elif browser == "opera":
            wd = webdriver.Opera().get(url_final)

        else:
            raise Exception("Browser not found")
    return wd


@pytest.fixture
def test_teardown(driver):
    driver.quit()
