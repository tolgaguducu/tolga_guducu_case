import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class QaJobsPage(BasePage):
    
    SEE_ALL_JOBS_BUTTON = (By.XPATH, "//a[normalize-space()='See all QA jobs']")
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    DEPARTMENT_FILTER = (By.ID, "select2-filter-by-department-container")
    JOB_LIST = (By.ID, "jobs-list")
    JOB_ITEMS = (By.CSS_SELECTOR, ".position-list-item")
    FIRST_JOB_ITEM = (By.CSS_SELECTOR, "#jobs-list > .position-list-item")
    VIEW_ROLE_BUTTON = (By.XPATH, "(//a[text()='View Role'])[1]")
    JOB_TITLE = (By.CSS_SELECTOR, ".position-title.font-weight-bold")
    JOB_DEPARTMENT = (By.CSS_SELECTOR, ".position-department.text-large.font-weight-600.text-primary")
    JOB_LOCATION = (By.CSS_SELECTOR, ".position-location.text-large")


    def go_to_qa_page(self):
        self.get_url("https://useinsider.com/careers/quality-assurance/")

    def click_see_all_jobs(self):
        see_all_jobs_btn = self._find_element(self.SEE_ALL_JOBS_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", see_all_jobs_btn)
        see_all_jobs_btn.click()
        time.sleep(1)

    def verify_department_and_filter_location(self, expected_department, location_to_select):
        with allure.step(f"Verifying Department is '{expected_department}' and filtering by Location '{location_to_select}'"):
            wait = WebDriverWait(self.driver, 15)
            self.logger.info(f"Waiting for department filter to be set to '{expected_department}'...")
            wait.until(EC.text_to_be_present_in_element(self.DEPARTMENT_FILTER, expected_department))
            self.logger.info(f"SUCCESS: Department is correctly pre-selected as '{expected_department}'.")
            self.logger.info(f"Selecting location: {location_to_select}")
            self._click(self.LOCATION_FILTER)
            location_option_locator = (By.XPATH, f"//li[@id and text()='{location_to_select}']")
            location_option = wait.until(EC.element_to_be_clickable(location_option_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", location_option)
            location_option.click()
            time.sleep(3)

    def is_job_list_present(self) -> bool:
        return self._is_visible(self.JOB_LIST)

    def get_all_job_details(self) -> list:
        job_details = []
        job_items = self.driver.find_elements(*self.JOB_ITEMS)
        for item in job_items:
            try:
                title = item.find_element(*self.JOB_TITLE).text
                department = item.find_element(*self.JOB_DEPARTMENT).text
                location = item.find_element(*self.JOB_LOCATION).text
                
                details = {
                    'title': title,
                    'department': department,
                    'location': location
                }
                job_details.append(details)
            except Exception as e:
                self.logger.warning(f"Could not retrieve details for a job item. Error: {e}")
                continue   
        return job_details

    def get_first_job_title_and_click_view_role(self) -> str:
        with allure.step("Get first job title, scroll, hover and click 'View Role'"):
            wait = WebDriverWait(self.driver, 10)
            self.logger.info("Scrolling to the job list.")
            job_list_element = self._find_element(self.JOB_LIST)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", job_list_element)
            self.logger.info("Finding the first job item.")
            first_job = self._find_element(self.FIRST_JOB_ITEM)
            job_title_text = first_job.find_element(*self.JOB_TITLE).text
            self.logger.info(f"Captured job title: {job_title_text}")
            self.logger.info("Hovering over the first job item.")
            actions = ActionChains(self.driver)
            actions.move_to_element(first_job).perform()
            self.logger.info("Waiting for the 'View Role' button to be clickable.")
            view_role_btn = wait.until(EC.element_to_be_clickable(self.VIEW_ROLE_BUTTON))
            view_role_btn.click()
            return job_title_text