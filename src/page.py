from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, MarketPlaceLocators, LoginPageLocators, RegistrationPageLocators, \
    AdminLoginPageLocators, AdminDashboardPageLocators, AdminAddProductPageLocators, AdminProductsPageLocators, \
    AdminCustomerListLocators, AddNewCustomerLocators
from common import wait_and_return_button


class MainPage:
    def is_logo_present(self, driver):
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(MainPageLocators.LOGO_BUTTON))
        return driver.find_element(*MainPageLocators.LOGO_BUTTON)

    def is_img_title_matches(self, driver):
        return driver.find_element(*MainPageLocators.LOGO_IMG).get_attribute("title")

    def is_free_download_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.FREE_DOWNLOAD_BUTTON)

    def is_visit_marketplace_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.MARKETPLACE_BUTTON)

    def is_view_demo_button_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.VIEWDEMO_BUTTON)

    def is_featured_section_present(self, driver):
        return wait_and_return_button(driver, MainPageLocators.LEARN_MORE_BUTTON)

    def is_learnmore_section_present2(self, driver):
        return driver.find_element(*MainPageLocators.LEARN_MORE_BUTTON)


class MarketPage:

    def is_marketheader_present(self, driver):
        return wait_and_return_button(driver, MarketPlaceLocators.MARKET_HEADER)

    def is_extension_category_present(self, driver):
        try:
            wait_and_return_button(driver, MarketPlaceLocators.SECTION_CATEGORY)
            found = True
        except:
            found = False
        return found

    def is_product_card_present(self, driver):
        return wait_and_return_button(driver, MarketPlaceLocators.PRODUCT_LINK)


class LoginPage:

    def is_login_form_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.LOGIN_FORM)

    def is_login_field_present(self, driver):
        return driver.find_element(*LoginPageLocators.LOGIN_FIELD)
        # return wait_and_return_button(driver, LoginPageLocators.LOGIN_FIELD)

    def is_password_field_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.PASSWORD_FIELD)

    def is_login_button_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.LOGIN_BUTTON)

    def is_forgot_link_present(self, driver):
        return wait_and_return_button(driver, LoginPageLocators.FORGOT_LINK)


class RegistrationPage:

    def is_username_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.USERNAME)

    def is_firstname_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.FIRSTNAME)

    def is_lastname_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.LASTNAME)

    def is_email_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.EMAIL)

    def is_country_field_present(self, driver):
        return wait_and_return_button(driver, RegistrationPageLocators.COUNTRY)


class AdminLoginPage:

    def is_admin_login_present(self, driver):
        return wait_and_return_button(driver, AdminLoginPageLocators.ADMINLOGIN)

    def is_admin_pswd_present(self, driver):
        return wait_and_return_button(driver, AdminLoginPageLocators.ADMINPSWD)

    def is_admin_loginbutton_present(self, driver):
        return wait_and_return_button(driver, AdminLoginPageLocators.LOGINBUTTON)


class DashboardPage:

    def is_admin_navigation_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.NAVIGATION)

    def is_admin_navmenu_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.NAVMENU)

    def is_admin_catalog_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.CATALOG)

    def is_admin_catalog_products_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.CATALOG_PRODUCTS)

    def is_admin_products_header_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.PRODUCTS_HEADER)

    def is_add_new_item_btn_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.ADD_NEW_BTN)

    def is_customers_in_catalog_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.CUSTOMERS)

    def is_customers_page_in_cat_present(self, driver):
        return wait_and_return_button(driver, AdminDashboardPageLocators.CUSTOMERS_SECTION)


class AddProductPage:

    def is_tab_general_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.GENERAL_TAB)

    def is_productname_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.PRODUCTNAME)

    def is_productname_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.PRODUCTNAME_INPUT)

    def is_descr_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.DESCR)

    def is_descr_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.DESCR_INPUT)

    def is_metatag_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGTITLE)

    def is_metatag_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGTITLE_INPUT)

    def is_metatagdescr_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGDESCR)

    def is_metategdescr_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGDESCR_INPUT)

    def is_metatagkeyw_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGKEYWRD)

    def is_metategkeyw_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.METATAGKEYWRD_INPUT)

    def is_producttag_field_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.PRODUCTTAGS)

    def is_producttag_input_present(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.PRODUCTTAGS_INPUT)

    def is_btn_save_product_prsent(self, driver):
        return wait_and_return_button(driver, AdminAddProductPageLocators.SAVE_BTN)


class RemoveProductPage:

    def is_filter_present(self, driver):
        return wait_and_return_button(driver, AdminProductsPageLocators.FILTER_NAME)

    def is_filter_btn_present(self, driver):
        return wait_and_return_button(driver, AdminProductsPageLocators.FILTER_BUTTON)

    def is_item_selector_present(self, driver):
        return wait_and_return_button(driver, AdminProductsPageLocators.CHECKBOX_SELECTOR)

    def is_delete_btn_present(self, driver):
        return wait_and_return_button(driver, AdminProductsPageLocators.DELETE_BTN)


class CustomersPage:

    def is_customer_list(self, driver):
        return wait_and_return_button(driver, AdminCustomerListLocators.CUSTOMERLIST)


class NewCustomerPage:

    def is_email_field_present(self, driver):
        return wait_and_return_button(driver, AddNewCustomerLocators.CUSTOMER_EMAIL)

    def is_phone_field_present(self, driver):
        return wait_and_return_button(driver, AddNewCustomerLocators.CUSTOMER_PHONE)

    def is_pswd_field_present(self, driver):
        return wait_and_return_button(driver, AddNewCustomerLocators.CUSTOMER_PSWD)

    def is_pswd_confirm_field_present(self, driver):
        return wait_and_return_button(driver, AddNewCustomerLocators.CUSTOMER_PSWD_CONFIRM)
