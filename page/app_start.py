from .default_page import DefaultPage
from setting import CAP, REMOTE_DIR
from appium.webdriver import Remote


class App:
    @staticmethod
    def init_driver():
        return Remote(REMOTE_DIR, CAP)

    def start(self):
        driver = self.init_driver()
        driver.implicitly_wait(10)
        return DefaultPage(driver)
