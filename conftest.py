import time
import logging
import pytest
import pathlib
from pathlib import Path
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", "-U", default="http://192.168.1.74:8081/")
    parser.addoption("--drivers", default=f"{Path(pathlib.Path.home())}/drivers")
    parser.addoption("--bv")
    parser.addoption("--vnc")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="192.168.1.74")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drivers = request.config.getoption("--drivers")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(f"===> Test {request.node.name} started at {time.asctime()}")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
    else:
        raise ValueError("Browser not supported!")

    driver = webdriver

    if executor == "local":
        '''
        Если хотим запустить тесты локально, без подъема сервера, то необходимо
        указать аргумент командной строки --executor local
        '''
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path=f"{drivers}/chromedriver.exe", options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=f"{drivers}/geckodriver.exe", options=options)
    elif executor:
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities={
                "browserName": browser_name,
                "browserVersion": version,
                "screenResolution": "1920x1080",
                "name": "Alexandr",
                "selenoid:options": {
                    "enableVNC": vnc
                },
                "timeZone": "Europe/Moscow",
                "goog:chromeOptions": {}
            })

    def open_browser():
        return driver.get(url)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info(f"Browser:{driver.name} --- Session: {driver.session_id}\n")

    driver.open = open_browser
    driver.open()

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info(f"===> Test {request.node.name} finished at {time.asctime()}\n\n")

    request.addfinalizer(fin)
    return driver
