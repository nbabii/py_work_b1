import pytest
from core.driver_manager import WebDriverManager


@pytest.fixture(scope="class")
def open_browser(request, browser_name):
    driver_manger = WebDriverManager(browser_name)
    driver = driver_manger.get_driver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser")