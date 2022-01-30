from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from otus_01.src.page import MainPage


def test_header(driver):
    try:
      #  WebDriverWait(driver, 20).until(EC.presence_of_element_located(LOGO_BUTTON))
       # brand = driver.find_element(LOGO_IMG)
        main_page = MainPage(driver)
        main_page.is_logo_present()
        assert main_page.is_logo_present().get_attribute("title") == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)
    finally:
        driver.quit()


def test_button_free_download(driver):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn.btn-success.btn-xl']")))
        brand = driver.find_element(By.XPATH, "//*[@class='btn.btn-success.btn-xl']")
        assert brand.getText() == 'OpenCart - Open Source Shopping Cart Solution'
    except TimeoutException:
        print(TimeoutException)
    finally:
        driver.quit()

 # import os
# browserExe = "chrome"
# os.system("pkill "+browserExe)
