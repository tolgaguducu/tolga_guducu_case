from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    LOCATIONS_BLOCK = (By.ID, "career-our-location")
    TEAMS_BLOCK = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[normalize-space()='Life at Insider']/ancestor::section[1]")
    
    def are_core_blocks_displayed(self) -> bool:
        locations_visible = self._is_visible(self.LOCATIONS_BLOCK)
        teams_visible = self._is_visible(self.TEAMS_BLOCK)
        life_at_insider_visible = self._is_visible(self.LIFE_AT_INSIDER_BLOCK)
        self.logger.info(f"Locations block visibility: {locations_visible}")
        self.logger.info(f"Teams block visibility: {teams_visible}")
        self.logger.info(f"Life at Insider block visibility: {life_at_insider_visible}")

        return locations_visible and teams_visible and life_at_insider_visible