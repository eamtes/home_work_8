import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from tests.DATA_for_tests.SELECTORS import Cart_Page


class CartPage(BasePage):

    @allure.step
    def go_to_checkout(self, wait=BasePage._WAIT):
        self._click_in_element(self._element(Cart_Page.BUTTONS), Cart_Page.CHECKOUT_LINK, wait)

    @allure.step
    def verify_product(self, product_name, wait=BasePage._WAIT):
        self._verify_element_presence(Cart_Page.CONTENT, wait)
        self._verify_element_presence((By.LINK_TEXT, product_name), wait)

    @allure.step
    def click_element_on_cart_page(self, element, wait=BasePage._WAIT):
        self._click_element(self._element(element, wait), wait)

    @allure.step
    def check_text_on_cart_page(self, xpath):
        self.check_text(xpath)
