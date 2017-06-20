import pytest
import unittest


class TestClassA:

    @pytest.mark.usefixtures("open_browser")
    def test_login(self):
        self.driver.get("https://www.fb.com")
        print("Test DONE")

