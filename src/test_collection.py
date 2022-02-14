from selenium.common.exceptions import TimeoutException

from locators import MainPageLocators
from page import MainPage


def test_header(driver):
    try:
        main_page = MainPage()
        main_page.is_logo_present(driver)
        assert main_page.is_img_title_matches(driver) == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)


def test_header_second_version(driver):
    text = driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")
    assert text == 'OpenCart - Open Source Shopping Cart Solution'


def test_button_free_download(driver):
        main_page = MainPage()
        main_page.is_free_download_button_present(driver)
        assert main_page.is_free_download_button_present(driver).get_attribute("innerHTML") == 'Download'


def test_visit_marketplace_button(driver):
    assert MainPage().is_visit_marketplace_button_present(driver).get_attribute("innerHTML") == 'Marketplace'


def test_view_demo_button(driver):
    text = MainPage().is_view_demo_button_present(driver).text
    assert text == 'DEMO'


def test_featured_section(driver):
    assert MainPage().is_featured_section_present(driver).text == 'LEARN MORE'

#какой формат записи лучше?
#works
#def test_learnmore_second(driver):
 #   text = driver.find_element(*MainPageLocators.LEARN_MORE_BUTTON).text
  #  assert text == 'LEARN MORE'

#works
#def test_lm_foth(driver):
 #   assert MainPage().is_learnmore_section_present2(driver).text == 'LEARN MORE'


def test_teardown(driver):
    driver.quit()
