import logging
import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _WAIT = 1

    def __init__(self, driver):
        self.driver = driver

        self.driver.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.driver.logger.handlers.clear()
        self.driver.logger.addHandler(file_handler)
        self.driver.logger.setLevel(level=self.driver.log_level)

    def _verify_element_presence(self, locator: tuple, wait: float = _WAIT):
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(locator))
            self.driver.logger.info(f"Confirmed the presence of the element on the page: {locator}\n")
        except TimeoutException:
            self.driver.logger.error(f"The presence of the element on the page was not confirmed: {locator}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"The presence of the element on the page was not confirmed: {locator}")
        else:
            return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(locator))

    def _verify_element_clickable(self, locator: tuple, wait: float = _WAIT):
        try:
            WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(locator))
            self.driver.logger.info(f"Element is clickable by locator: {locator}\n")
        except TimeoutException:
            self.driver.logger.error(f"Element not clickable by locator: {locator}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Element  not clickable by locator: {locator}")

    def _element(self, locator: tuple, wait: float = _WAIT):
        return self._verify_element_presence(locator, wait)

    def _elements(self, locator: tuple):
        try:
            self.driver.find_elements(*locator)
            self.driver.logger.info(f"Elements found by locator: {locator}\n")
        except NoSuchElementException:
            self.driver.logger.error(f"Found not elements by locator: {locator}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Found not elements by locator: {locator}")
        else:
            return self.driver.find_elements(*locator)

    def _element_in_elements(self, element, locator: tuple):
        try:
            element.find_element(*locator)
            self.driver.logger.info(f"Element found by locator: {locator}\n")
        except NoSuchElementException:
            self.driver.logger.error(f"Found not element by locator: {locator}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Found not element by locator: {locator}")
        else:
            return element.find_element(*locator)

    def _move_to_element(self, element, wait: float = _WAIT):
        try:
            ActionChains(self.driver).pause(wait).move_to_element(element).perform()
            self.driver.logger.info(f"Cursor set to element by locator: {element}\n")
        except TimeoutException:
            self.driver.logger.error(f"Found not element by locator: {element}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Found not element by locator: {element}")

    def _click_element(self, element, wait: float = _WAIT):
        try:
            ActionChains(self.driver).pause(wait).move_to_element(element).click().perform()
            self.driver.logger.info(f"Click to element: {element}\n")
        except TimeoutException:
            self.driver.logger.error(f"Found not element by locator: {element}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Found not element by locator: {element}")

    def _click_in_element(self, element, locator: tuple, index: int = 0, wait: float = _WAIT):
        try:
            element = element.find_elements(*locator)[index]
            self._click_element(wait, element)
            self.driver.logger.info(f"Click to element: {element}\n")
        except NoSuchElementException:
            self.driver.logger.error(f"Found not element by locator: {element}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Found not element by locator: {element}")

    def check_text(self, xpath):
        try:
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_xpath(xpath)
            self.driver.logger.info(f"Text found by locator: {xpath}\n")
        except NoSuchElementException:
            self.driver.logger.error(f"Text not found by locator: {xpath}\n")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Text not found by locator: {xpath}")
