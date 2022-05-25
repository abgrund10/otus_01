import json
import os
from datetime import datetime
import allure
import pytest
import logging

from packaging.requirements import URI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='http://www.opencart.com')
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--way_to_execute', action='store', default='localhost')


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
    else:
        url_final = "http://127.0.0.2:4444/wd/hub"  # .format(runner=runner)
        caps = {
            "browserName": "chrome",
            "screenResolution": "1280x1024",
            "name": "agr tests"
        }
        wd = webdriver.Remote(url_final, desired_capabilities=caps)
        print(caps)
    return wd


@pytest.fixture
def test_teardown(driver, url):
    driver.quit()