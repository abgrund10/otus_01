from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from common import wait_and_return_button


class MainPage:
    def is_logo_present(self, driver):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(MainPageLocators.LOGO_BUTTON))
        return driver.find_element(*MainPageLocators.LOGO_BUTTON)

    def is_img_title_matches(self, driver):
        return driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")

    def is_free_download_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.FREE_DOWNLOAD_BUTTON)

    def is_visit_marketplace_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.MARKETPLACE_BUTTON)
