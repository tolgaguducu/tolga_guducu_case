from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", headless=False):

        browser = browser.lower()

        if browser == "chrome":
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--log-level=3")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options,
            )

        else:
            raise ValueError(f"'{browser}' is not supported")

        driver.implicitly_wait(10)

        return driver