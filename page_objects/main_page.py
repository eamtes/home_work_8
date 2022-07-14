import allure

from page_objects.base_page import BasePage
from tests.DATA_for_tests.SELECTORS import Main_Page


class MainPage(BasePage):

    @allure.step
    def verify_element_clickable_on_main_page(self, locator, wait=BasePage._WAIT):
        return self._verify_element_clickable(locator, wait)

    @allure.step
    def visibility_of_element_on_main_page(self, locator, wait=BasePage._WAIT):
        return self._verify_element_presence(locator, wait)

    @allure.step
    def click_featured_product_on_main_page(self, number, wait=BasePage._WAIT):
        feature_product = self._elements(Main_Page.FEATURE_PRODUCT)[number]
        product_name = self._element_in_elements(feature_product, Main_Page.FEATURE_PRODUCT_NAME).text
        self._click_element(feature_product, wait)
        return product_name

    @allure.step
    def click_element_on_main_page(self, element, wait=BasePage._WAIT):
        self._click_element(self._element(element, wait), wait)

    @allure.step
    def move_to_element_on_main_page(self, element, wait=BasePage._WAIT):
        self._move_to_element(self._element(element, wait), wait)

    @allure.step
    def check_text_on_main_page(self, xpath):
        self.check_text(xpath)
