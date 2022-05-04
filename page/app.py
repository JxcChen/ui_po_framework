from .default_page import DefaultPage
from setting import CAP, REMOTE_DIR
from appium.webdriver import Remote
from .base_page import BasePage
from .main import Main


class App(BasePage):
    # 指定包名和activity
    _package = ""
    _activity = ""

    @staticmethod
    def init_driver():
        return Remote(REMOTE_DIR, CAP)

    def start(self):
        if self._driver is None:
            self._driver = self.init_driver()
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(app_package=self._package,app_activity=self._activity)
        # 返回当前对象
        return self

    def main(self):
        """
        进入主页面
        :return: MainPage
        """
        return Main(self._driver)
