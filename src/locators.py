from selenium.webdriver.common.by import By


class LoginPage(object):
    SIGNIN = "/html/body/div[1]/div[1]/main/article/div/div/div/div[1]/div[2]/button[2]"
    Insta_link = 'a[href="https://www.instagram.com/"]'
    Sign = '//a[@href="/sign-in"]'


class SignPage(object):
    BackButton = 'a[href="/"]'
    Error = "//div[@data-error='Обязательное поле']"
    Email = 'email'
    Password = "password"
    Password2 = 'passwordConfirmation'
    SIGNIN = 'p-button-label.p-c'


class City(object):
    Perm = "//li[@aria-label='Пермь']"
    Confirm = 'p-button-label.p-c'


class Requests(object):
    filters_open = '/html/body/div[1]/div[1]/section[2]/div/div/div[1]/div/div'
    filters_close = 'p-dialog-header-close-icon.pi.pi-times'
    my = '/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div'
    tournaments = "//*[contains(text(), 'Турниры')]"
