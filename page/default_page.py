from appium.webdriver.common.mobileby import MobileBy
from .contact.contact_page import ContactPage

from page.base_page import BasePage

bottom_selector = (MobileBy.ID, "f0d")
contact_btn = (MobileBy.XPATH, "//*[@text='通讯录']")
msg_btn = (MobileBy.XPATH, "//*[@text='信息']")
back_btn = (MobileBy.ID, "iwk")


class DefaultPage(BasePage):
    def into_contact_page(self):
        self.click(contact_btn)
        return ContactPage(self.driver)

    def back_to_default_page(self):
        try:
            self.driver.find_element(*bottom_selector)
        except Exception as e:
            self.back()
            self.back_to_default_page()
        else:
            self.click(msg_btn)
            return self

    def back(self):
        self.click(back_btn)
