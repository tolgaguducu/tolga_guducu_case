# tests/conftest.py
import pytest
import allure
import logging
from allure_commons.types import AttachmentType
from utils.driver_factory import DriverFactory
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def driver(request):
    web_driver = DriverFactory.get_driver(browser="chrome")
    
    yield web_driver

    if request.node.rep_call.failed:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name=f"Failure_Screenshot_{timestamp}",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as e:
            logging.warning(f"Error while attaching screenshot to Allure report: {e}")

    logging.info("--- Test finished, closing browser ---")
    web_driver.quit()