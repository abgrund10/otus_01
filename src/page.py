from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators
from otus_01.src.conftest import driver


class MainPage(driver):
    def is_logo_present(self):
        """Triggers the search"""
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(*MainPageLocators.LOGO_BUTTON)
        logo = driver.find_element(*MainPageLocators.LOGO_IMG)
        return logo