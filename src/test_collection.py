import pytest
from locators import MainPageLocators
from page import MainPage, MarketPage, LoginPage, RegistrationPage

LOGIN_URL = 'https://www.opencart.com/index.php?route=account/login'
REGISTER_URL = 'https://www.opencart.com/index.php?route=account/register'
ADMIN_URL = 'https://demo.opencart.com/admin/'


def test_header(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        main_page = MainPage()
        main_page.is_logo_present(driver)
        assert main_page.is_img_title_matches(driver) == 'OpenCart - Open Source Shopping Cart Solution'
    else:
        pytest.skip()


def test_header_second_version(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        text = driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")
        assert text == 'OpenCart - Open Source Shopping Cart Solution'
    else:
        pytest.skip()


def test_button_free_download(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        main_page = MainPage()
        main_page.is_free_download_button_present(driver)
        assert main_page.is_free_download_button_present(driver).get_attribute("innerHTML") == 'Download'
    else:
        pytest.skip()


def test_visit_marketplace_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        assert MainPage().is_visit_marketplace_button_present(driver).get_attribute("innerHTML") == 'Marketplace'
    else:
        pytest.skip()


def test_view_demo_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        text = MainPage().is_view_demo_button_present(driver).text
        assert text == 'DEMO'
    else:
        pytest.skip()
