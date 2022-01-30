import webbrowser

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(url, browser):
    try:
        # webbrowser.get(browser).open_new(url)
        stroka = "webdriver.{browser}()".format(browser=browser)
        driver = eval(stroka)
        driver.get(url)
    except Exception:
        raise Exception
    return driver


def test_header(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand')))
        brand = driver.find_element(By.CSS_SELECTOR, "img[src='application/view/image/icon/opencart-logo.png']")
        assert brand.get_attribute("title") == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)
    finally:
        driver.quit()


def test_button_free_download(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn.btn-success.btn-xl']")))
        brand = driver.find_element(By.XPATH, "//*[@class='btn.btn-success.btn-xl']")
        assert brand.getText() == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)
    finally:
        driver.quit()

 # import os
# browserExe = "chrome"
# os.system("pkill "+browserExe)
