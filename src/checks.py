from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.opencart.com/'
browser = 'Firefox'


def find_smth(url, browser):
    stroka = "webdriver.{browser}()".format(browser=browser)
    driver = eval(stroka)
    driver.get(url)
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand')))
        brand = driver.find_element(By.CSS_SELECTOR, "img[src='application/view/image/icon/opencart-logo.png']")
        assert brand.get_attribute("title") == 'OpenCart - Open Source Shopping Cart Solution'
    finally:
        driver.quit()


find_smth(url, browser)
