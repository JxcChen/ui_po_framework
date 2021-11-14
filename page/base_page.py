import os
import time

from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from common.exception_handle import ExceptionHandle
from common.path_handle import IMG_PATH
from common.log_handle import log


class BasePage:

    def __init__(self, driver: Remote):
        self.driver = driver
        self.current_element = None

    def screenshot(self, image_desc):
        """
        错误截图
        :param image_desc: 截图描述
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        try:
            self.driver.save_screenshot(os.path.join(IMG_PATH, image_desc + now + ".jpg"))
        except Exception as e:
            log.exception(f"{image_desc}截图失败")
            raise e
        else:
            log.info(f"{image_desc}截图成功")

    def get_element(self, loc, image_desc=""):
        """
        获取元素
        :param loc: 元素定位  type：元祖
        :param image_desc: 失败截图描述
        """
        try:
            self.current_element = self.driver.find_element(*loc)
        except Exception as e:
            # 进行失败重试
            page_source = self.driver.page_source
            if ExceptionHandle.max_time > ExceptionHandle.retry_time:
                for handle in ExceptionHandle.get_all_handle():
                    if handle.is_hit(page_source):
                        handle.handle(self.driver)
                        ExceptionHandle.retry_time += 1
                        self.get_element(loc, image_desc)
            # 重试结束 未找到对应元素进行错误截图
            log.exception("未能找到{}元素{}".format(image_desc, loc))
            self.screenshot(image_desc)
            raise e
        else:
            log.info("获取{}元素{}成功".format(image_desc, loc))
            return self

    def wait_element_visible(self, loc, timeout=20, frequency_time=0.2, image_desc=""):
        """
        等待元素可见
        :param loc: 元素定位
        :param timeout: 等待时间
        :param frequency_time: 轮训时间
        :param image_desc: 失败截图描述
        :return: self
        """
        try:
            self.current_element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency_time).until(
                ec.visibility_of_element_located(loc))
        except Exception as e:
            # 进行失败重试
            page_source = self.driver.page_source
            if ExceptionHandle.max_time > ExceptionHandle.retry_time:
                for handle in ExceptionHandle.get_all_handle():
                    if handle.is_hit(page_source):
                        handle.handle(self.driver)
                        ExceptionHandle.retry_time += 1
                        self.get_element(loc, image_desc)
            # 重试结束 未找到对应元素进行错误截图
            log.exception("未能找到{}元素{}".format(image_desc, loc))
            self.screenshot(image_desc)
            raise e
        else:
            log.info("获取{}元素{}成功".format(image_desc, loc))
            return self

    def wait_element_exist(self, loc, timeout=20, frequency_time=0.2, image_desc=""):
        """
        等待元素可见
        :param loc: 元素定位
        :param timeout: 等待时间
        :param frequency_time: 轮训时间
        :param image_desc: 失败截图描述
        :return: self
        """
        try:
            self.current_element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency_time).until(
                ec.presence_of_element_located(loc))
        except Exception as e:
            # 进行失败重试
            page_source = self.driver.page_source
            if ExceptionHandle.max_time > ExceptionHandle.retry_time:
                for handle in ExceptionHandle.get_all_handle():
                    if handle.is_hit(page_source):
                        handle.handle(self.driver)
                        ExceptionHandle.retry_time += 1
                        self.get_element(loc, image_desc)
            # 重试结束 未找到对应元素进行错误截图
            log.exception("未能找到{}元素{}".format(image_desc, loc))
            self.screenshot(image_desc)
            raise e
        else:
            log.info("获取{}元素{}成功".format(image_desc, loc))
            return self

    def click(self, loc="", image_desc=""):
        """
        点击元素
        :param loc: 元素定位
        :param image_desc: 截图描述
        :return: self
        """
        if loc != "":
            self.get_element(loc, image_desc).click()
        else:
            self.current_element.click()
        return self

    def send_date(self, loc="", date="", image_desc=""):
        """
        输入内容
        :param date: 输入的内容
        :param loc: 元素定位
        :param image_desc: 截图描述
        :return: self
        """
        if loc != "":
            self.get_element(loc, image_desc).current_element.send_keys(date)
        else:
            self.current_element.send_keys(date)
        return self

    def get_text(self, loc="", image_desc=""):
        """
        获取元素属性
        :param loc: 元素定位
        :param image_desc: 截图描述
        :return: self
        """
        if loc != "":
            text = self.get_element(loc, image_desc).current_element.text
        else:
            text = self.current_element.text
        return text

    def get_attribute(self, loc="", attr="", image_desc=""):
        """
        获取元素属性
        :param loc: 元素定位
        :param attr: 目标属性
        :param image_desc: 截图描述
        :return: self
        """
        if loc != "":
            attribute = self.get_element(loc, image_desc).current_element.get_attributd(attr)
        else:
            attribute = self.current_element.get_attribute(attr)
        return attribute

    def swipe(self, direction):
        """
        向指方向置滑动
        :param direction:  方向
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        if direction == "up":
            self.driver.swipe(start_x=width * 0.5, start_y=height * 0.2, end_x=width * 0.5, end_y=height * 0.8,
                              direction=100)
        elif direction == "down":
            self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                              duration=100)
        elif direction == "left":
            self.driver.swipe(start_x=width * 0.2, start_y=height * 0.5, end_x=width * 0.8, end_y=height * 0.5,
                              duration=100)
        elif direction == "right":
            self.driver.swipe(start_x=width * 0.8, start_y=height * 0.5, end_x=width * 0.2, end_y=height * 0.5,
                              duration=100)
        return self

    def swipe_to_element_exist(self, loc, image_desc):
        """
        滑动到元素可见
        :param loc: 元素定位
        :param image_desc: 截图描述
        :return: self
        """
        old_source = self.driver.page_source
        while True:
            try:
                self.current_element = self.driver.find_element(*loc)
            except Exception as e:
                self.swipe("down")
                new_source = self.driver.page_source
                if old_source == new_source:
                    log.exception(f"已经滑到底部,未能找到{image_desc}元素")
                    self.screenshot(image_desc)
                    raise e
                else:
                    old_source = new_source
            else:
                break
        return self
