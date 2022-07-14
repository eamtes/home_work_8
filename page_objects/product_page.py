import allure

from page_objects.base_page import BasePage


class ProductPage(BasePage):

    @allure.step
    def click_element_on_product_page(self, element, wait=BasePage._WAIT):
        self._click_element(self._element(element, wait), wait)
