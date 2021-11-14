from page.base_page import BasePage

from page_locator.contact import add_member_page_loc


class AddMemberPage(BasePage):
    def add_member(self, name, phone_number):
        """
        添加成员
        :param name: 成员名称
        :param phone_number: 成员手机号
        :return: contact_page
        """
        self.send_date(add_member_page_loc.nameInput, date=name, image_desc="输入名称").send_date(
            add_member_page_loc.phoneInput, date=phone_number, image_desc="输入手机号").click(add_member_page_loc.saveBtn,
                                                                                         "点击保存按钮")
        from .contact_page import ContactPage
        return ContactPage(self.driver)
