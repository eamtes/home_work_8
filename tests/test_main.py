import time
import pytest
import allure
from page_objects.register_page import RegisterPage
from page_objects.cart_page import CartPage
from page_objects.product_page import ProductPage
from page_objects.user_page import UserPage
from page_objects.catalog_page import CatalogPage
from page_objects.elements.success_alert import SuccessAlert
from page_objects.main_page import MainPage
from page_objects.cart_product_page import CartProductPage
from page_objects.login_page import LoginPage
from tests.DATA_for_tests.SELECTORS import Success_Alert, Cart_Page, Cart_Product_Page, Catalog_Page, Login_Page, \
    Main_Page, Product_Page, Register_Page, User_Page
from tests.DATA_for_tests.DATA_INPUT import Data_Register_Page, User_For_Adding_New_Product, User_For_Removing_product


@allure.title("Проверка наличия элементов на главной странице")
@pytest.mark.parametrize("CSS_SELECTORS", [Main_Page.IMG_MACBOOK,
                                           Main_Page.IMG_IPHONE,
                                           Main_Page.SEARCH,
                                           Main_Page.CART_TOTAL,
                                           Main_Page.LINK_TEXT_OPENCART])
def test_main_page(browser, CSS_SELECTORS):
    with allure.step("Шаг 1: Проверка наличия элементов на главной странице"):
        MainPage(browser).visibility_of_element_on_main_page(CSS_SELECTORS)


@allure.title("Проверка наличия элементов на странице каталога")
@pytest.mark.parametrize("CSS_SELECTORS", [Catalog_Page.INPUT_LIMIT,
                                           Catalog_Page.INPUT_SORT,
                                           Catalog_Page.LIST_VIEV,
                                           Catalog_Page.GRID_VIEV,
                                           Catalog_Page.COLUMN_LEFT])
def test_catalog_page(browser, CSS_SELECTORS):
    with allure.step("Шаг 1: Наведение мыши на элемент"):
        MainPage(browser).move_to_element_on_main_page(Main_Page.BUTTON_DESKTOPS)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_SHOW_ALL_DESKTOPS)
    with allure.step("Шаг 3: Проверка наличия элементов на главной странице"):
        CatalogPage(browser).visibility_of_element_on_cp(CSS_SELECTORS)


@allure.title("Проверка наличия элементов на странице продукта")
@pytest.mark.parametrize("CSS_SELECTORS", [Cart_Product_Page.DOT,
                                           Cart_Product_Page.LINK_HP,
                                           Cart_Product_Page.BUTTON_CART,
                                           Cart_Product_Page.INPUT_OPTION_255,
                                           Cart_Product_Page.BUTTON_ONCLICK_COMPARE])
def test_cart_product_page(browser, CSS_SELECTORS):
    with allure.step("Шаг 1: Наведение мыши на элемент"):
        MainPage(browser).move_to_element_on_main_page(Main_Page.BUTTON_DESKTOPS)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_SHOW_ALL_DESKTOPS)
    with allure.step("Шаг 3: Клик на элемент"):
        CatalogPage(browser).click_element_on_cp(Catalog_Page.LAPTOP_HP_3065)
    with allure.step("Шаг 4: Проверка наличия элементов на главной странице"):
        CartProductPage(browser).visibility_of_element_on_cart_product_page(CSS_SELECTORS)


@allure.title("Проверка наличия элементов на странице логина")
@pytest.mark.parametrize("CSS_SELECTORS", [Login_Page.LINK_REGISTER,
                                           Login_Page.INPUT_LOGIN,
                                           Login_Page.PLACEHOLDER_MAIL,
                                           Login_Page.PLACEHOLDER_PASSWORD,
                                           Login_Page.LINK_FORGOTTEN])
def test_login_page(browser, CSS_SELECTORS):
    time.sleep(1)
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_LOGIN)
    with allure.step("Шаг 3: Проверка наличия элементов на главной странице"):
        LoginPage(browser).visibility_of_element_on_login_page(CSS_SELECTORS)


@allure.title("Проверка наличия элементов на странице регистрации")
@pytest.mark.parametrize("CSS_SELECTORS", [Register_Page.SUBSCRIBE_YES,
                                           Register_Page.SUBSCRIBE_NO,
                                           Register_Page.CHECKBOX_PRIVACY_POLICY,
                                           Register_Page.BUTTON_CONTINUE,
                                           Register_Page.LINK_PRIVACY_POLICY])
def test_register_page(browser, CSS_SELECTORS):
    time.sleep(1)
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_REGISTER)
    with allure.step("Шаг 3: Проверка наличия элементов на главной странице"):
        RegisterPage(browser).visibility_of_element_on_register_page(CSS_SELECTORS)


@allure.story("OpenCart - работа с корзиной")
@allure.title("Сценарий добавления продукта в корзину пользователем")
def test_adding_new_product(browser):
    time.sleep(1)
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_LOGIN)
    with allure.step("Шаг 3: Ввод логина и пароля"):
        UserPage(browser).login_with(User_For_Adding_New_Product.LOGIN, User_For_Adding_New_Product.PASSWORD)
    with allure.step("Шаг 4: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(User_Page.BACK_TO_MAIN_PAGE)
    with allure.step("Шаг 5: Клик на элемент"):
        product_name = MainPage(browser).click_featured_product_on_main_page(0)
    with allure.step("Шаг 6: Клик на элемент"):
        ProductPage(browser).click_element_on_product_page(Product_Page.ADD_TO_CART_BUTTON)
    with allure.step("Шаг 7: Клик на элемент"):
        SuccessAlert(browser).click_element_on_success_alert(Success_Alert.SOPPING_CART)
    with allure.step("Шаг 8: Подтверждение продукта"):
        CartPage(browser).verify_product(product_name)
    with allure.step("Шаг 9: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 10: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_LOGOUT)
    with allure.step("Шаг 11: Проверка текста"):
        MainPage(browser).check_text_on_main_page(Login_Page.TEXT_ACCOUNT_LOGOUT)
    with allure.step("Шаг 12: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Login_Page.BUTTON_CONTINUE_FOR_LOGOUT)


@allure.story("OpenCart - работа с корзиной")
@allure.title("Сценарий очистки корзины пользователем")
def test_removing_product_from_the_list(browser):
    time.sleep(1)
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_LOGIN)
    with allure.step("Шаг 3: Ввод логина и пароля"):
        UserPage(browser).login_with(User_For_Removing_product.LOGIN, User_For_Removing_product.PASSWORD)
    with allure.step("Шаг 4: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(User_Page.BACK_TO_MAIN_PAGE)
    with allure.step("Шаг 5: Клик на элемент"):
        product_name = MainPage(browser).click_featured_product_on_main_page(0)
    with allure.step("Шаг 6: Клик на элемент"):
        ProductPage(browser).click_element_on_product_page(Product_Page.ADD_TO_CART_BUTTON)
    with allure.step("Шаг 7: Клик на элемент"):
        SuccessAlert(browser).click_element_on_success_alert(Success_Alert.SOPPING_CART)
    with allure.step("Шаг 8: Подтверждение продукта"):
        CartPage(browser).verify_product(product_name)
    with allure.step("Шаг 9: Клик на элемент"):
        CartPage(browser).click_element_on_cart_page(Cart_Page.BUTTON_REMOVE)
    with allure.step("Шаг 10: Проверка текста"):
        CartPage(browser).check_text_on_cart_page(Cart_Page.TEXT_CART_IS_EMPTY)
    time.sleep(1)
    with allure.step("Шаг 11: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 12: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_LOGOUT)
    with allure.step("Шаг 13: Проверка текста"):
        MainPage(browser).check_text_on_main_page(Login_Page.TEXT_ACCOUNT_LOGOUT)
    with allure.step("Шаг 14: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Login_Page.BUTTON_CONTINUE_FOR_LOGOUT)


@allure.story("OpenCart - работа с авторизацией")
@allure.title("Сценарий регистрации нового пользователя")
def test_new_user_registration(browser):
    time.sleep(1)
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_MY_ACCOUNT)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_REGISTER)
    with allure.step("Шаг 3: Заполнение поля 'Имя'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.FIRST_NAME, Register_Page.FIELD_FIRST_NAME)
    with allure.step("Шаг 4: Заполнение поля 'Фамилия'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.LAST_NAME, Register_Page.FIELD_LAST_NAME)
    with allure.step("Шаг 5: Заполнение поля 'Электронная почта'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.EMAIL, Register_Page.FIELD_EMAIL)
    with allure.step("Шаг 6: Заполнение поля 'Телефон'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.TELEPHONE, Register_Page.FIELD_TELEPHONE)
    with allure.step("Шаг 7: Заполнение поля 'Пароль'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.PASSWORD, Register_Page.FIELD_PASSWORD)
    with allure.step("Шаг 8: Заполнение поля 'Подтверждение пароля'"):
        RegisterPage(browser).send_key_on_register_page(Data_Register_Page.PASSWORD_CONFIRM,
                                                        Register_Page.FIELD_PASSWORD_CONFIRM)
    with allure.step("Шаг 9: Клик на элемент"):
        RegisterPage(browser).click_element_on_register_page(Register_Page.CHECKBOX_PRIVACY_POLICY)
    with allure.step("Шаг 10: Клик на элемент"):
        RegisterPage(browser).click_element_on_register_page(Register_Page.BUTTON_CONTINUE)
    with allure.step("Шаг 11: Проверка наличия элементов на главной странице"):
        RegisterPage(browser).visibility_of_element_on_register_page(Register_Page.BUTTON_SUCCESS)
    with allure.step("Шаг 12: Клик на элемент"):
        RegisterPage(browser).click_element_on_register_page(Register_Page.BUTTON_CONTINUE_AFTER_REGISTRATION)


@allure.story("OpenCart - работа с валютой")
@allure.title("Сценарий смены цены в разной валюте")
def test_currency_switching(browser):
    with allure.step("Шаг 1: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_CURRENCY)
    with allure.step("Шаг 2: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.CURRENCY_POUND_STERLING)
    with allure.step("Шаг 3: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_CURRENCY)
    with allure.step("Шаг 4: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.CURRENCY_US_DOLLAR)
    with allure.step("Шаг 5: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.BUTTON_CURRENCY)
    with allure.step("Шаг 6: Клик на элемент"):
        MainPage(browser).click_element_on_main_page(Main_Page.CURRENCY_EURO)
