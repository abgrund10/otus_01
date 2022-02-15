from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, MarketPlaceLocators, LoginPageLocators, RegistrationPageLocators
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

    def is_view_demo_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.VIEWDEMO_BUTTON)

    def is_featured_section_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.LEARN_MORE_BUTTON)

    def is_learnmore_section_present2(self, driver):
        return driver.find_element(*MainPageLocators.LEARN_MORE_BUTTON)


class MarketPage:

    def is_marketheader_present(self, driver):
        return wait_and_return_button(driver, MarketPlaceLocators.MARKET_HEADER)

    def is_extension_category_present(self, driver):
        try:
            wait_and_return_button(driver, MarketPlaceLocators.SECTION_CATEGORY)
            found = True
        except:
            found = False
        return found

    def is_product_card_present(self, driver):
        try:
            wait_and_return_button(driver, MarketPlaceLocators.PRODUCT_LINK)
            found = True
        except:
            found = False
        return found


class LoginPage:

    def is_login_form_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.LOGIN_FORM)

    def is_login_field_present(self, driver):
        return driver.find_element(*LoginPageLocators.LOGIN_FIELD)
        #return wait_and_return_button(driver, LoginPageLocators.LOGIN_FIELD)

    def is_password_field_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.PASSWORD_FIELD)

    def is_login_button_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.LOGIN_BUTTON)

    def is_forgot_link_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.FORGOT_LINK)


class RegistrationPage:

    def is_username_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.USERNAME)

    def is_firstname_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.FIRSTNAME)

    def is_lastname_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.LASTNAME)

    def is_email_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.EMAIL)

    def is_country_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.COUNTRY)
