import allure
from locators import LoginPage, SignPage, City, Requests
import random

n = random.randint(0, 220)


@allure.feature('Login page')
@allure.story('Validation of page objects')
@allure.title('Validation of main page')
@allure.step("SignIn option is present")
def test_main_page(driver):
    try:
        driver.find_element_by_css_selector(LoginPage.Insta_link)
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of back button')
@allure.step('Validation of functionality of return')
def test_signin_back(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_css_selector(SignPage.BackButton).click()
        assert driver.find_element_by_css_selector(LoginPage.Insta_link)
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin')
@allure.step('Validation of signin errors')
def test_signin_errors(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
        assert driver.find_element_by_xpath(SignPage.Error)
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid email")
def test_signin_invalid_email(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys("@atp.com")
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_name(SignPage.Password2).send_keys("1234567")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid password")
def test_signin_invalid_password(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys("any@attp.com")
        driver.find_element_by_name(SignPage.Password).send_keys("123")
        driver.find_element_by_name(SignPage.Password2).send_keys("123")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid confirmation")
def test_signin_invalid_confirmation(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys("second2@attp.com")
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_name(SignPage.Password2).send_keys("1234987")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers successfully")
def test_signin_successful(driver):
    random_email = "second" + f'{n}' + "@attp.com"
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys(random_email)
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_name(SignPage.Password2).send_keys("1234567")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Get location')
@allure.step("User selects location")
def test_signin_location(driver):
    random_email2 = "second" + f'{n + 1}' + "@attp.com"
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys(random_email2)
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_name(SignPage.Password2).send_keys("1234567")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(City.Perm).click()
        driver.find_element_by_class_name(City.Confirm).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('User cannot see functionality')
@allure.step("User signups with existing creds")
def test_existing_creds(driver):
    try:
        driver.find_element_by_xpath(LoginPage.SIGNIN).click()
        driver.find_element_by_id(SignPage.Email).click()
        driver.find_element_by_id(SignPage.Email).send_keys("second2@attp.com")
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_name(SignPage.Password2).send_keys("1234567")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('User can use functionality')
@allure.step("User observes filters")
def test_requests(driver):
    try:
        driver.find_element_by_css_selector(LoginPage.Sign).click()
        driver.find_element_by_id(SignPage.Email).send_keys("second2@attp.com")
        driver.find_element_by_name(SignPage.Password).send_keys("1234567")
        driver.find_element_by_class_name(SignPage.SIGNIN).click()
        driver.find_element_by_xpath(Requests.filters_open).click()
        driver.find_element_by_class_name(Requests.filters_close).click()
        driver.find_element_by_xpath(Requests.my).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)
