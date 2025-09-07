import allure
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QaJobsPage
from pages.lever_page import LeverPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Career Page Tests")
class TestCareerApplication:

    @allure.title("Verify End-to-End Career Page Journey for QA Position in Istanbul")
    @allure.description("This test verifies the user journey of finding a QA job in Istanbul and navigating to the application form.")
    def test_insider_career_flow(self, driver):
        
        home_page = HomePage(driver)
        careers_page = CareersPage(driver)
        qa_jobs_page = QaJobsPage(driver)
        lever_page = LeverPage(driver)
        
        with allure.step("Step 1: Visit home page and verify it is opened"):
            home_page.load()
            home_page.accept_cookies()
            assert "Insider" in driver.title, "Home page title does not include 'Insider'"
            assert home_page.is_navigation_bar_visible(), "Navigation bar is not visible on the home page."

        with allure.step("Step 2: Navigate to Careers page and check for core blocks"):
            home_page.navigate_to_careers_page()
            assert careers_page.are_core_blocks_displayed(), "Core blocks are not visible."

        with allure.step("Step 3: Go to QA jobs, filter, and check for the jobs list"):
            qa_jobs_page.go_to_qa_page()
            qa_jobs_page.click_see_all_jobs()
            qa_jobs_page.verify_department_and_filter_location(expected_department="Quality Assurance", location_to_select="Istanbul, Turkiye")
            assert qa_jobs_page.is_job_list_present(), "Job list is not present after filtering."

        with allure.step("Step 4: Check that all jobs' details are correct"):
            all_jobs = qa_jobs_page.get_all_job_details()
            assert len(all_jobs) > 0, "No jobs found in the list after filtering."
            for job in all_jobs:
                with allure.step(f"Verifying Job: {job['title']}"):
                    assert "Quality Assurance" in job["title"], f"Position (title) does not contain 'Quality Assurance' for job: {job['title']}"
                    assert "Quality Assurance" in job["department"], f"Department does not contain 'Quality Assurance' for job: {job['title']}"
                    assert "Istanbul, Turkiye" in job["location"], f"Location is not 'Istanbul, Turkiye' for job: {job['title']}"

        with allure.step("Step 5: Click 'View Role' and check redirection and job title."):
            expected_job_title = qa_jobs_page.get_first_job_title_and_click_view_role()
            initial_window_handle = driver.current_window_handle
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            all_window_handles = driver.window_handles
            new_window_handle = [h for h in all_window_handles if h != initial_window_handle][0]
            driver.switch_to.window(new_window_handle)
            WebDriverWait(driver, 10).until(EC.url_contains("lever.co"))
            current_url = driver.current_url
            assert "lever.co" in current_url, f"Redirected URL '{current_url}' does not contain 'lever.co'"
            assert lever_page.is_job_title_correct(expected_job_title), "Job title on Lever page does not match the selected job."