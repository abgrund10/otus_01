import pytest
from selenium.webdriver.support.ui import Select
from locators import MainPageLocators
from page import MainPage, MarketPage, LoginPage, RegistrationPage

LOGIN_URL = 'https://www.opencart.com/index.php?route=account/login'
REGISTER_URL = 'https://www.opencart.com/index.php?route=account/register'


def test_header(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        main_page = MainPage()
        main_page.is_logo_present(driver)
        assert main_page.is_img_title_matches(driver) == 'OpenCart - Open Source Shopping Cart Solution'
    else:
        pytest.skip()


def test_header_second_version(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        text = driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")
        assert text == 'OpenCart - Open Source Shopping Cart Solution'
    else:
        pytest.skip()


def test_button_free_download(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        main_page = MainPage()
        main_page.is_free_download_button_present(driver)
        assert main_page.is_free_download_button_present(driver).get_attribute("innerHTML") == 'Download'
    else:
        pytest.skip()


def test_visit_marketplace_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MainPage().is_visit_marketplace_button_present(driver).get_attribute("innerHTML") == 'Marketplace'
    else:
        pytest.skip()


def test_view_demo_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        text = MainPage().is_view_demo_button_present(driver).text
        assert text == 'DEMO'
    else:
        pytest.skip()


def test_featured_section(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MainPage().is_featured_section_present(driver).text == 'LEARN MORE'


def test_see_marketplace_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        MainPage().is_visit_marketplace_button_present(driver).click()
        assert MarketPage().is_marketheader_present(driver).text == 'Welcome to OpenCart Extension Store'
    else:
        pytest.skip()


def test_marketplace_categories_present(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MarketPage().is_extension_category_present(driver) == True
    else:
        pytest.skip()


def test_marketplace_productcard(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MarketPage().is_product_card_present(driver) == True
    else:
        pytest.skip()


def test_login_page_form_present(driver, url):
    if url == LOGIN_URL:
        LoginPage().is_login_form_present(driver)
        LoginPage().is_login_field_present(driver).send_keys('password')
        LoginPage().is_password_field_present(driver).send_keys('password')
        LoginPage().is_forgot_link_present(driver).click()


def test_check_registration_form(driver, url):
    if url == REGISTER_URL:
        RegistrationPage().is_username_field_present(driver).send_keys('myusername')
        RegistrationPage().is_firstname_field_present(driver).send_keys('myfirstname')
        RegistrationPage().is_lastname_field_present(driver).send_keys('mylastname')
        RegistrationPage().is_email_field_present(driver).send_keys('email@email.com')
        dropdown = Select(RegistrationPage().is_country_field_present(driver))
        RegistrationPage().is_country_field_present(driver).click()
        dropdown.select_by_index(1)


def test_teardown(driver, url):
    driver.quit()
