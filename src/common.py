import urllib
import webbrowser

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from otus_01.src.page import RemoveProductPage


def wait_and_return_button(driver, button):
    try:
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(button))
        return element
    except TimeoutException:
        print(button)


def open_url(url):
    return webbrowser.open(url, new=0, autoraise=True)


def filter_item(driver, filter_item):
    RemoveProductPage().is_filter_present(driver).send_keys(filter_item)
    return RemoveProductPage().is_filter_btn_present(driver).click()


