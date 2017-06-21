import pytest
import unittest
from pages.main_page import MainPage
import time


@pytest.mark.usefixtures("open_browser")
class TestClassA(unittest.TestCase):

    def test_main(self):
        self.driver.get("http://automationpractice.com/index.php")
        main_page = MainPage(self.driver)
        main_page.navigate_to_login().enter_login("TEST")
        print("Test DONE")

    def test_login(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        print("Test DONE")
