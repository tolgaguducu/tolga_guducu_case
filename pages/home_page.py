from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and normalize-space()='Company']")
    CAREERS_LINK = (By.CSS_SELECTOR, "a[class='dropdown-sub'][href='https://useinsider.com/careers/']")
    ACCEPT_COOKIES_BUTTON = (By.ID, "wt-cli-accept-all-btn")
    
    def load(self):
        self.get_url("https://useinsider.com/")

    def accept_cookies(self):
        if self._is_visible(self.ACCEPT_COOKIES_BUTTON):
            self._click(self.ACCEPT_COOKIES_BUTTON)
            
    def is_navigation_bar_visible(self) -> bool:
        self.logger.info("Checking if the main navigation bar is visible.")
        return self._is_visible(self.COMPANY_MENU)

    def navigate_to_careers_page(self):
        company_menu_element = self._find_element(self.COMPANY_MENU)
        careers_link_element = self._find_element(self.CAREERS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(company_menu_element).click(careers_link_element).perform()