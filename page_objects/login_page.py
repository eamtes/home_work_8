import allure

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    @allure.step
    def visibility_of_element_on_login_page(self, locator, wait=BasePage._WAIT):
        return self._verify_element_presence(locator, wait)
