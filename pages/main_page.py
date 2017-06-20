import utils.custom_logger as page_logger
import logging
from pages.base_page import BasePage
from pages.login_page import LoginPage


class MainPage(BasePage):

    # Locators
    _LOGIN_BUTTON = "//*[@class='login']"

    log = page_logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login(self):
        self.log.debug("Clicking on login link")
        self.driver.find_element_by_xpath(self._LOGIN_BUTTON).click()
        return LoginPage(self.driver)
