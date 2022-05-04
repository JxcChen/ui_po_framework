from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.contact.contact_page import ContactPage

contact_btn = (MobileBy.XPATH, "//*[@text='通讯录']")


class Main(BasePage):

    def into_contact(self):
        """
        进入通讯录页面
        :return: contact_page
        """
        self.click(contact_btn)
        return ContactPage(self._driver)
