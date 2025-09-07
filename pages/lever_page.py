import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeverPage(BasePage):
    JOB_TITLE_HEADER = (By.CSS_SELECTOR, "div.posting-headline > h2")
    
    @allure.step("Verifying job title on Lever page")
    def is_job_title_correct(self, expected_title: str) -> bool:
        try:
            actual_title = self._find_element(self.JOB_TITLE_HEADER).text
            self.logger.info(f"Found job title on Lever page: '{actual_title}'")
            return expected_title == actual_title
        except Exception as e:
            self.logger.error(f"Could not find job title on Lever page. Error: {e}")
            return False