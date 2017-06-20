from enum import Enum


class Browser(Enum):
    ie_short = "ie"
    ie_full = "iexplorer"
    ff_short = "ff"
    ff_full = "firefox"
    ch_short = "ch"
    ch_full = "chrome"

    @staticmethod
    def get_values():
        values = []
        for browser in Browser:
            values.append(browser.value)
        return values

