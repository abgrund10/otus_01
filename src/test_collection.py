import allure
import pytest
from selenium.webdriver.support.ui import Select
from locators import MainPageLocators
from page import MainPage, MarketPage, LoginPage, RegistrationPage

LOGIN_URL = 'https://www.opencart.com/index.php?route=account/login'
REGISTER_URL = 'https://www.opencart.com/index.php?route=account/register'
ADMIN_URL = 'https://demo.opencart.com/admin/'


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of header')
@allure.step("Logo is present")
def test_header(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        main_page = MainPage()
        main_page.is_logo_present(driver)
        try:
            assert main_page.is_img_title_matches(driver) == 'OpenCart - Open Source Shopping Cart Solution'
        except AssertionError:
            allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)
    else:
        pytest.skip()


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of header')
@allure.step("Title matches expected text")
def test_header_second_version(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        text = driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")
        try:
            assert text == 'OpenCart - Open Source Shopping Cart Solution'
        except AssertionError:
            allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)
    else:
        pytest.skip()


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check if button free download is present")
def test_button_free_download(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        main_page = MainPage()
        main_page.is_free_download_button_present(driver)
        try:
            assert main_page.is_free_download_button_present(driver).get_attribute("innerHTML") == 'Download'
        except AssertionError:
            allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)
    else:
        pytest.skip()


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check if there is marketplace button")
def test_visit_marketplace_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        assert MainPage().is_visit_marketplace_button_present(driver).get_attribute("innerHTML") == 'Marketplace'
    else:
        pytest.skip()


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check if there is view demo button")
def test_view_demo_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        text = MainPage().is_view_demo_button_present(driver).text
        assert text == 'DEMO'
    else:
        pytest.skip()


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('Validation of text')
@allure.step("Check if section learn more present")
def test_featured_section(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        assert MainPage().is_featured_section_present(driver).text == 'LEARN MORE'


@allure.feature('Market page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check if there is OpenCart Extension Store")
def test_see_marketplace_button(driver, url):
    if not any((REGISTER_URL, LOGIN_URL, ADMIN_URL)):
        MainPage().is_visit_marketplace_button_present(driver).click()
        assert MarketPage().is_marketheader_present(driver).text == 'Welcome to OpenCart Extension Store'


@allure.feature('Market page')
@allure.story('Validation of page objects')
@allure.title('Validation of categories')
@allure.step("Check if there is extension")
def test_marketplace_categories_present(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MarketPage().is_extension_category_present(driver) == True
    else:
        pytest.skip()


@allure.feature('Market page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check if there is marketplace cards")
def test_marketplace_productcard(driver, url):
    if not any((REGISTER_URL, LOGIN_URL)):
        assert MarketPage().is_product_card_present(driver) == True
    else:
        pytest.skip()


@allure.feature('Login page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
def test_login_page_form_present(driver, url):
    if url == LOGIN_URL:
        LoginPage().is_login_form_present(driver)
        LoginPage().is_login_field_present(driver).send_keys('password')
        LoginPage().is_password_field_present(driver).send_keys('password')
        LoginPage().is_forgot_link_present(driver).click()


@allure.feature('Registration page')
@allure.story('Validation of page objects')
@allure.title('Validation of button')
@allure.step("Check registration form")
def test_check_registration_form(driver, url):
    if url == REGISTER_URL:
        RegistrationPage().is_username_field_present(driver).send_keys('myusername')
        RegistrationPage().is_firstname_field_present(driver).send_keys('myfirstname')
        RegistrationPage().is_lastname_field_present(driver).send_keys('mylastname')
        RegistrationPage().is_email_field_present(driver).send_keys('email@email.com')
        dropdown = Select(RegistrationPage().is_country_field_present(driver))
        RegistrationPage().is_country_field_present(driver).click()
        dropdown.select_by_index(1)