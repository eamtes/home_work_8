import allure

from page_objects.base_page import BasePage


class CatalogPage(BasePage):

    @allure.step
    def visibility_of_element_on_cp(self, locator, wait=BasePage._WAIT):
        return self._verify_element_presence(locator, wait)

    @allure.step
    def click_element_on_cp(self, locator, wait=BasePage._WAIT):
        self._click_element(self._element(locator, wait), wait)

    @allure.step
    def move_to_element_on_cp(self, element, wait=BasePage._WAIT):
        self._move_to_element(self._element(element, wait), wait)
