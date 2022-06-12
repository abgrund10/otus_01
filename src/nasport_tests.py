from telnetlib import EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginpageN, SignPage, City, Requests

url = "https://nasport.fun/"


@allure.feature('Login page')
@allure.story('Validation of page objects')
@allure.title('Validation of main page')
@allure.step("SignIn option is present")
def test_main_page(driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(LoginpageN.INSTAGRAMLINK))
        driver.find_element(LoginpageN.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of back button')
@allure.step('Validation of functionality of return')
def test_signin_back(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.BackButton).click()
        assert driver.find_element(LoginpageN.INSTAGRAMLINK)
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin')
@allure.step('Validation of signin errors')
def test_signin_errors(driver):
    try:
        driver.find_element(LoginpageN.SIGNIN).click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.SIGNIN).click()
        assert driver.find_element(SignPage.Error)
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid email")
def test_signin_invalid_email(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.Email).click()
        driver.find_element(SignPage.Email).send_keys("@atp.com")
        driver.find_element(SignPage.Password).send_keys("1234567")
        driver.find_element(SignPage.Password2).send_keys("1234567")
        driver.find_element(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid password")
def test_signin_invalid_password(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.Email).click()
        driver.find_element(SignPage.Email).send_keys("second@attp.com")
        driver.find_element(SignPage.Password).send_keys("123")
        driver.find_element(SignPage.Password2).send_keys("123")
        driver.find_element(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers with invalid confirmation")
def test_signin_cinvalid_onfirmation(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.Email).click()
        driver.find_element(SignPage.Email).send_keys("second@attp.com")
        driver.find_element(SignPage.Password).send_keys("1234567")
        driver.find_element(SignPage.Password2).send_keys("1234987")
        driver.find_element(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Validation of signin function')
@allure.step("User registers successfully")
def test_signin_successful(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(SignPage.Email))
        driver.find_element(SignPage.Email).click()
        driver.find_element(SignPage.Email).send_keys("second@attp.com")
        driver.find_element(SignPage.Password).send_keys("1234567")
        driver.find_element(SignPage.Password2).send_keys("1234567")
        driver.find_element(SignPage.SIGNIN).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('SignIn page')
@allure.story('Validation of page objects')
@allure.title('Get location')
@allure.step("User selects location")
def test_signin_location(driver):
    try:
        driver.find_element(City.Perm).click()
        driver.find_element(City.Confirm).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Main page')
@allure.story('Validation of page objects')
@allure.title('User can use functionality')
@allure.step("User observes filters")
def test_requests(driver):
    try:
        driver.find_element(Requests.filters_open).click()
        driver.find_element(Requests.filters_close).click()
        driver.find_element(Requests.my).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Requests page')
@allure.story('Validation of page objects')
@allure.title('User can use functionality')
@allure.step("User opens tournaments")
def test_tournaments(driver):
    try:
        driver.find_element(Requests.tournaments).click()
    except AssertionError:
        allure.attach("screenshot", attachment_type=allure.attachment_type.PNG)
