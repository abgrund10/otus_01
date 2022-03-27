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


class AdminLoginPageLocators(object):
    ADMINLOGIN = (By.NAME, "username")
    ADMINPSWD = (By.NAME, "passwords")
    LOGINBUTTON = (By.XPATH, "//button[@type='submit']")


class AdminDashboardPageLocators(object):
    NAVIGATION = (By.XPATH, "//div[@id='navigation']")
    NAVMENU = (By.XPATH, "//ul[@id='menu']")
    CATALOG = (By.XPATH, "//li[@id='menu-catalog']")
    CATALOG_PRODUCTS = (By.XPATH, "//li[@id='menu-catalog']//a[text()='Products']")
    CUSTOMERS = (By.XPATH, "//ul[@id='menu-customers']")
    CUSTOMERS_SECTION = (By.XPATH, "//li[@id='menu-customers']//a[text()='Customers']")
    PRODUCTS_HEADER = (By.XPATH, "//ul[@class='breadcrumb']//a[text()='Products']")
    ADD_NEW_BTN = (By.XPATH, "//a[@data-original-title='Add New']")


class AdminAddProductPageLocators(object):
    GENERAL_TAB = (By.XPATH, "//a[@data-toggle='tab']")
    PRODUCTNAME = (By.XPATH, "//label[@for='input-name1']")
    PRODUCTNAME_INPUT = (By.XPATH, "//input[@id='input-name1']")
    DESCR = (By.XPATH, "//label[@for='input-description1']")
   # DESCR = (By.CLASS_NAME, "note-editable.panel-body")
   # DESCR_INPUT = (By.XPATH, "//div[@class='note-editable.panel-body']")
    DESCR_INPUT = (By.CLASS_NAME, "note-editable.panel-body")
    METATAGTITLE = (By.XPATH, "//label[@for='input-meta-title1']")
    METATAGTITLE_INPUT = (By.XPATH, "//input[@id='input-meta-title1']")
    METATAGDESCR = (By.XPATH, "//label[@for='input-meta-description1']")
    METATAGDESCR_INPUT = (By.XPATH, "//textarea[@id='input-meta-description1']")
    METATAGKEYWRD = (By.XPATH, "//label[@for='input-meta-keyword1']")
    METATAGKEYWRD_INPUT = (By.XPATH, "//textarea[@id='input-meta-keyword1']")
    PRODUCTTAGS = (By.XPATH, "//span[@data-original-title='Comma separated']")
    PRODUCTTAGS_INPUT = (By.XPATH, "//input[@id='input-tag1']")
    SAVE_BTN = (By.XPATH, "//button[@data-original-title='Save']")


class AdminProductsPageLocators(object):
    DELETE_BTN = (By.XPATH, "//button[@data-original-title='Delete']")
    FILTER_NAME = (By.XPATH, "//input[@name='filter_name']")
    FILTER_BUTTON = (By.XPATH, "//button[@id='button-filter']")
    CHECKBOX_SELECTOR = (By.XPATH, "//input[@type='checkbox']")

class AdminCustomerListLocators(object):
    CUSTOMERLIST = (By.XPATH, "//h3[@class='panel-title']")

class AddNewCustomerLocators(object):
  #  CUSTOMER_FIRSTNAME =
  #  CUSTOMER_LASTNAME =
    CUSTOMER_EMAIL = (By.XPATH, "//input[@id='input-email']")
    CUSTOMER_PHONE = (By.XPATH, "//input[@id='input-telephone']")
    CUSTOMER_PSWD = (By.XPATH, "//input[@id='input-password']")
    CUSTOMER_PSWD_CONFIRM = (By.XPATH, "//input[@id='input-confirm']")
