import allure

from page_objects.base_page import BasePage


class SuccessAlert(BasePage):

    @allure.step
    def click_element_on_success_alert(self, element, wait=1):
        self._click_element(self._element(element, wait), wait)
