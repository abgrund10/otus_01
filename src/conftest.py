from datetime import datetime
import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='http://www.opencart.com')
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--way_to_execute', action='store', default='localhost')
    parser.addoption('--browser_version', action='store', default='latest')


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
    browserversion = request.config.getoption("--browser_version")
    if runner == 'localhost':
        url_final = url
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument(browserversion)
            wd = webdriver.Chrome(chrome_options=options).get(url_final)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument(browserversion)
            wd = webdriver.Firefox(firefox_options=firefox_options).get(url_final)
        elif browser == "opera":
            wd = webdriver.Opera().get(url_final)

        else:
            raise Exception("Browser not found")
    else:
        url_final = f"http://{runner}:4444/wd/hub"
        caps = {
            "browserName": "chrome",
            "screenResolution": "1280x1024",
            "name": "agr tests"
        }
        wd = webdriver.Remote(url_final, desired_capabilities=caps)
        print(caps)
    return wd


@allure.step("Verify element {button} on page.")
def wait_and_return_button(wd, button):
    try:
        element = WebDriverWait(wd, 20).until(EC.visibility_of_element_located(button))
        return element
    except AssertionError:
        allure.attach(name=wd.session_id, body=wd.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        raise AssertionError(f"Element {button} not found on page!")


@pytest.fixture
def test_teardown(driver, url):
    driver.quit()
