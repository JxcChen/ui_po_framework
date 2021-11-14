from appium.webdriver import Remote
from selenium.webdriver.common.by import By


class ExceptionHandle:
    retry_time = 0
    max_time = 3

    def is_hit(self, page_source):
        pass

    def handle(self, driver):
        pass

    @classmethod
    def get_all_handle(cls):
        handle_list = [PopupHandle(), UpgradeHandle(), out_desktop_handle()]
        return handle_list


class PopupHandle(ExceptionHandle):
    """
    app无响应 继续等待
    """

    def is_hit(self, page_source):
        if "无响应" in page_source:
            return True
        return False

    def handle(self, driver: Remote):
        driver.find_element(By.XPATH, "//*[@text='等待']").click()


class UpgradeHandle(ExceptionHandle):
    """
    升级弹框点击取消  具体样式看app本身
    """

    def is_hit(self, page_source):
        if "升级" in page_source:
            return True
        return False

    def handle(self, driver):
        driver.find_element(By.XPATH, "//*[@text=否]").click()


class out_desktop_handle(ExceptionHandle):
    """
    以外弹出桌面
    """

    def is_hit(self, page_source):
        # todo: 判断页面内容 是否弹出桌面
        if "" in page_source:
            pass

    def handle(self, driver: Remote):
        # todo: 弹出桌面则回到app中
        driver.start_activity(app_package="", app_activity="")
