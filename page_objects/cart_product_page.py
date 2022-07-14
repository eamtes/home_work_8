import allure

from page_objects.base_page import BasePage


class CartProductPage(BasePage):

    @allure.step
    def visibility_of_element_on_cart_product_page(self, locator, wait=BasePage._WAIT):
        return self._verify_element_presence(locator, wait)
