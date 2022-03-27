import pytest
from selenium.webdriver.support.ui import Select
from page import MainPage, MarketPage, LoginPage, RegistrationPage, AdminLoginPage, DashboardPage, AddProductPage, \
    RemoveProductPage, CustomersPage, NewCustomerPage

ADMIN_URL = 'https://demo.opencart.com/admin/'


def common_filter_item(driver, text):
    RemoveProductPage().is_filter_present(driver).send_keys(text)
    return RemoveProductPage().is_filter_btn_present(driver).click()


def test_admin_login(driver):
    AdminLoginPage().is_admin_login_present(driver).clear()
    AdminLoginPage().is_admin_pswd_present(driver).clear()
    AdminLoginPage().is_admin_login_present(driver).send_keys('demo')
    AdminLoginPage().is_admin_pswd_present(driver).send_keys('demo')
    AdminLoginPage().is_admin_loginbutton_present(driver).click()
    assert DashboardPage().is_admin_navigation_present(driver)
    assert DashboardPage().is_admin_navmenu_present(driver)


def test_open_products_page(driver):
    DashboardPage().is_admin_catalog_present(driver).click()
    DashboardPage().is_admin_catalog_products_present(driver).click()
    assert DashboardPage().is_admin_products_header_present(driver).get_attribute("innerHTML") == 'Products'


def test_add_new_product(driver):
    DashboardPage().is_add_new_item_btn_present(driver).click()
    assert AddProductPage().is_tab_general_present(driver).get_attribute("innerHTML") == 'General'
    assert AddProductPage().is_productname_field_present(driver).get_attribute("innerHTML") == 'Product Name'
    AddProductPage().is_productname_input_present(driver).send_keys('Nasport Product')
    assert AddProductPage().is_descr_field_present(driver).get_attribute("innerHTML") == 'Description'
    AddProductPage().is_descr_input_present(driver).send_keys('Nasport Description')
    assert AddProductPage().is_metatag_field_present(driver).get_attribute("innerHTML") == 'Meta Tag Title'
    AddProductPage().is_metatag_input_present(driver).send_keys('Nasport Meta Tag Title')
    assert AddProductPage().is_metatagdescr_field_present(driver).get_attribute("innerHTML") == 'Meta Tag Description'
    AddProductPage().is_metategdescr_input_present(driver).send_keys('Nasport Meta Tag Description')
    assert AddProductPage().is_metatagkeyw_field_present(driver).get_attribute("innerHTML") == 'Meta Tag Keywords'
    AddProductPage().is_metategkeyw_input_present(driver).send_keys('Nasport Meta Tag Keywords')
    assert AddProductPage().is_producttag_field_present(driver).get_attribute("innerHTML") == 'Product Tags'
    AddProductPage().is_producttag_input_present(driver).send_keys('Nasport Product Tags')
    AddProductPage().is_btn_save_product_prsent(driver).click()


def test_remove_product(driver):
    common_filter_item(driver, 'Nasport Product')
    RemoveProductPage().is_item_selector_present(driver).click()
    RemoveProductPage().is_delete_btn_present(driver).click()


def test_items_is_removed(driver):
    common_filter_item(driver, 'Nasport Product')
    assert len(RemoveProductPage().is_item_selector_present(driver)) == 0


def test_add_new_customer(driver):
    DashboardPage().is_customers_in_catalog_present(driver).click()
    DashboardPage().is_customers_page_in_cat_present(driver).click()
    assert CustomersPage().is_customer_list(driver).get_attribute("innerHTML") == 'Customer List'
    DashboardPage().is_add_new_item_btn_present(driver).click()
    RegistrationPage().is_firstname_field_present(driver).send_keys('Nasport First')
    RegistrationPage().is_lastname_field_present(driver).send_keys('Nasport Last')
    NewCustomerPage().is_email_field_present(driver).send_keys('info@nasport.fun')
    NewCustomerPage().is_phone_field_present(driver).send_keys('+79311220789')
    NewCustomerPage().is_pswd_field_present(driver).send_keys('MyfirstPasd')
    NewCustomerPage().is_pswd_confirm_field_present(driver).send_keys('MyfirstPasd')
    AddProductPage().is_btn_save_product_prsent(driver).click()

def test_new_customer_is_added(driver):
    common_filter_item(driver, 'Nasport First')
    assert len(RemoveProductPage().is_item_selector_present(driver)) != 0
