from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    LOGO_BUTTON = (By.CLASS_NAME, 'navbar-brand')
    LOGO_IMG = (By.CSS_SELECTOR, "img[src='application/view/image/icon/opencart-logo.png']")
    FREE_DOWNLOAD_BUTTON = (By.XPATH, "//*[@class='btn.btn-success.btn-xl']")
    MARKETPLACE_BUTTON = (By.XPATH, "//*[@class='btn.btn-primary.btn-xl']")

