import allure
from selenium.webdriver.common.by import By
from page_objects.elements.user_login_form import UserLoginForm
from page_objects.base_page import BasePage
from tests.DATA_for_tests.SELECTORS import User_Page


class UserPage(BasePage):

    @allure.step
    def login_with(self, username, password, wait=BasePage._WAIT):
        UserLoginForm(self.driver).login_with(username, password, wait)

    @allure.step
    def click_link(self, link_text, wait=BasePage._WAIT):
        self._click_element((By.LINK_TEXT, link_text), wait)

    @allure.step
    def verify_pay_form(self, wait=BasePage._WAIT):
        self._verify_element_presence(User_Page.PAYMENT_FORM, wait)

    @allure.step
    def verify_product_link(self, product_name, wait=BasePage._WAIT):
        self._verify_element_presence((By.LINK_TEXT, product_name), wait)

    @allure.step
    def click_element_on_user_page(self, element, wait=BasePage._WAIT):
        self._click_element(self._element(element, wait), wait)
