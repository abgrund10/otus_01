import json
import os
from datetime import datetime
import allure
import pytest
import logging
from selenium import webdriver


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
        url_final = f"http://{runner}:4444/wd/hub"
        caps = {
                "browserName": browser,
                "screenResolution": "1280x1024",
                "name": "agr tests",
                "selenoid:options": {
                    "sessionTimeout": "60s"
                }
            }
        wd = webdriver.Remote(command_executor=url_final, desired_capabilities=caps)
    allure.attach(body=json.dumps(wd), attachment_type=allure.attachment_type.JSON)
    return wd


@pytest.fixture
def test_teardown(driver, url):
    driver.quit()
