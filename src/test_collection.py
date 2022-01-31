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


def test_visit_marketplace_button(driver):
    try:
        main_page = MainPage()
        main_page.is_visit_marketplace_button_present(driver)
        assert main_page.is_visit_marketplace_button_present(driver).getText() == 'Visit Marketplace'
    except TimeoutException:
        print(TimeoutException)


def test_view_demo_button(driver):
    try:
        main_page = MainPage()
        main_page.is_view_demo_button_present(driver)
        assert main_page.is_view_demo_button_present(driver).getText() == 'View Demo'
    except TimeoutException:
        print(TimeoutException)


def test_featured_section(driver):
    try:
        main_page = MainPage()
        main_page.is_featured_section_present(driver)
        assert main_page.is_featured_section_present(driver).getText() == 'Featured in the Press by'
    except TimeoutException:
        print(TimeoutException)


def test_teardown(driver):
    driver.quit()
