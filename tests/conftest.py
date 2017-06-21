import pytest
from core.driver_manager import WebDriverManager
from utils.screenshot_helpper import ScreenshotHelper


driver = None


@pytest.fixture(scope="function")
def open_browser(request, browser_name):
    global driver
    driver_manger = WebDriverManager(browser_name)
    driver = driver_manger.get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    driver = None


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


def pytest_exception_interact(node, call, report):
    if report.failed:
        ScreenshotHelper.take_screen_on_fail(driver)
