from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    LOGO_BUTTON = (By.CLASS_NAME, 'navbar-brand')
    LOGO_IMG = (By.CSS_SELECTOR, "img[src='application/view/image/icon/opencart-logo.png']")
    FREE_DOWNLOAD_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=cms/download']")
    MARKETPLACE_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=marketplace/extension']")
    VIEWDEMO_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=cms/demo']")
    LEARN_MORE_BUTTON = (By.XPATH, "//a[@href='http://forum.opencart.com']")


class MarketPlaceLocators(object):
    MARKET_HEADER = (By.TAG_NAME, 'h1')
    SECTION_CATEGORY = (By.ID, 'extension-category')
    PRODUCT_LINK = (
    By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=38358']")


class LoginPageLocators(object):
    LOGIN_FORM = (By.XPATH, "//form[@action='https://www.opencart.com/index.php?route=account/login']")
    LOGIN_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGOT_LINK = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=account/forgotten']")


class RegistrationPageLocators(object):
    USERNAME = (By.NAME, "username")
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    COUNTRY = (By.NAME, "country_id")
