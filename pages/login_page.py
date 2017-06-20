import utils.custom_logger as page_logger
import logging
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    _LOGIN_INPUT = ".//*[@id='email']"

    log = page_logger.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, login):
        self.log.debug("Typing login: " + login)
        self.driver.find_element_by_xpath(self._LOGIN_INPUT).send_keys(login)