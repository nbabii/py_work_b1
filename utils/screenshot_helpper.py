import time
import os


class ScreenshotHelper:

    @staticmethod
    def take_screen_on_fail(driver):
        current_date = str(time.strftime("%d_%m_%Y"))
        current_time = str(time.strftime("%H_%M_%S"))
        current_ms = str(int(round(time.time() * 1000 % 1000)))
        dir_path = "screenshots" + os.path.sep + "failed" + os.path.sep + current_date + os.path.sep
        directory = os.path.dirname(dir_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        driver.get_screenshot_as_file(dir_path + current_time + "_" + current_ms + ".png")
