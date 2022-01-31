from selenium.common.exceptions import TimeoutException
from page import MainPage


def test_header(driver):
    try:
        main_page = MainPage()
        main_page.is_logo_present(driver)
        assert main_page.is_img_title_matches(driver) == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)


def test_button_free_download(driver):
    try:
        main_page = MainPage()
        main_page.is_free_download_button_present(driver)
        assert main_page.is_free_download_button_present(driver).getText() == 'Free Download'
    except TimeoutException:
        print(TimeoutException)


def test_teardown(driver):
    driver.quit()
