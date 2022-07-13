import allure

from page_objects.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step
    def visibility_of_element_on_register_page(self, locator, wait=BasePage._WAIT):
        return self._verify_element_presence(locator, wait)

    @allure.step
    def send_key_on_register_page(self, key, element, wait=BasePage._WAIT):
        self._verify_element_presence(element, wait).send_keys(key)

    @allure.step
    def click_element_on_register_page(self, element, wait=BasePage._WAIT):
        self._click_element(self._element(element, wait), wait)
