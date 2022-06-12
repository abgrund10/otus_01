from selenium.webdriver.common.by import By


class LoginpageN(object):
    SIGNIN = (By.CLASS_NAME, 'p-button-label p-c')
    INSTAGRAMLINK = (By.LINK_TEXT, "Instagram")


class SignPage(object):
    BackButton = (By.LINK_TEXT, "/")
    Error = (By.XPATH, 'div/[@data_error="Обязательное поле"]')  # Huston
    Email = (By.ID, 'email')
    Password = (By.NAME, "password")
    Password2 = (By.NAME, 'passwordConfirmation')
    SIGNIN = (By.CLASS_NAME, 'p-button-label p-c')


class City(object):
    Perm = (By.XPATH, 'aria-label="Пермь"')  # Huston
    Confirm = (By.CLASS_NAME, 'p-button-label p-c')


class Requests(object):
    filters_open = (By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/div')
    filters_close = (By.CLASS_NAME, 'p-dialog-header-close-icon.pi.pi-times')
    my = (By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div')
    tournaments = (By.XPATH, "//*[contains(text(), 'Турниры')]")
