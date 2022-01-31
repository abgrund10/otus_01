from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_and_return_button(driver, button):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(button))
    return driver.find_element(button)
