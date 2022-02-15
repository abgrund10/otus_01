import urllib
import webbrowser

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_and_return_button(driver, button):
    try:
        element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(button))
        return element
    except TimeoutException:
        print(button)


def open_url(url):
    return webbrowser.open(url, new=0, autoraise=True)

#    return driver.find_element(button) - или это лучше?

