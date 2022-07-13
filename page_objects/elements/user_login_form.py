import allure

from page_objects.base_page import BasePage
from tests.DATA_for_tests.SELECTORS import User_Login_Form


class UserLoginForm(BasePage):

    @allure.step
    def login_with(self, username, password, wait=BasePage._WAIT):
        self._verify_element_presence(User_Login_Form.INPUT_EMAIL, wait).send_keys(username)
        self._verify_element_presence(User_Login_Form.INPUT_PASSWORD, wait).send_keys(password)
        self.driver.find_element(*User_Login_Form.LOGIN_BUTTON).click()
