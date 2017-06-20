from selenium import webdriver


class WebDriverManager:

    def __init__(self, browser_name=None):
        if browser_name is not None:
            self.browser_name = browser_name
        else:
            self.browser_name = "firefox"

    def get_driver(self):
        if self.browser_name == "ie" or self.browser_name == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser_name == "ch" or self.browser_name == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_name == "ff" or self.browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception("Wrong --browser parameter set")
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
