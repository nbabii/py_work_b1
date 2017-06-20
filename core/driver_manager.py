from selenium import webdriver
from core.browsers_enum import Browser

class WebDriverManager:

    def __init__(self, browser_name=None):
        if browser_name is not None:
            self.browser_name = browser_name
        else:
            self.browser_name = "firefox"

    def get_driver(self):
        if self.browser_name == Browser.ie_short.value or self.browser_name == Browser.ie_full.value:
            driver = webdriver.Ie()
        elif self.browser_name == Browser.ch_short.value or self.browser_name == Browser.ch_full.value:
            driver = webdriver.Chrome()
        elif self.browser_name == Browser.ff_short.value or self.browser_name == Browser.ff_full.value:
            driver = webdriver.Firefox()
        else:
            raise Exception("Wrong '--browser' parameter value was set, available options: "
                            + str(Browser.get_values()))
        driver.implicitly_wait(5)
        driver.set_page_load_timeout(10)
        driver.maximize_window()
        return driver
