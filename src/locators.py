from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    LOGO_BUTTON = (By.CLASS_NAME, 'navbar-brand')
    LOGO_IMG = (By.CSS_SELECTOR, "img[src='application/view/image/icon/opencart-logo.png']")
    FREE_DOWNLOAD_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=cms/download']")
    MARKETPLACE_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=marketplace/extension']")
    VIEWDEMO_BUTTON = (By.XPATH, "//a[@href='https://www.opencart.com/index.php?route=cms/demo']")
    LEARN_MORE_BUTTON = (By.XPATH, "//a[@href='http://forum.opencart.com']")
