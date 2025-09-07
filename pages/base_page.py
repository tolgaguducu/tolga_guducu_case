import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)

    def _find_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        self.logger.info(f"Finding element with locator: {locator}")
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator: tuple, timeout: int = 10):
        self.logger.info(f"Clicking on element with locator: {locator}")
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(locator)).click()
    
    def _is_visible(self, locator: tuple, timeout: int = 10) -> bool:
        self.logger.info(f"Checking visibility of element: {locator}")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element {locator} is visible.")
            return True
        except Exception as e:
            self.logger.warning(f"Element {locator} is not visible.")
            return False

    def get_url(self, url: str):
        self.logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)