from page.base_page import BasePage
from .add_member_page import AddMemberPage
from page_locator.contact import contact_page_loc
from entity.member import member


class ContactPage(BasePage):

    def add_member(self, name, phone_number):
        """
        添加成员
        :param name: 成员名称
        :param phone_number: 手机号码
        :return: self
        """
        self.into_add_member_page().add_member(name, phone_number).back()
        return self

    def into_add_member_page(self):
        """
        进入添加成员页面
        :return:
        """
        self.swipe_to_element_exist(contact_page_loc.addMemberBtn, "下滑到添加成员按钮出").click(image_desc="点击添加成员").click(
            contact_page_loc.addManuallyBtn, "点击手动添加")
        return AddMemberPage(self.driver)

    def back(self):
        self.click(contact_page_loc.backButton, image_desc="点击返回按钮")
        return self

    def search(self, name):
        self.click(contact_page_loc.searchBtn, "点击搜索按钮").send_date(contact_page_loc.searchInput, date=name,
                                                                   image_desc="搜索框中输入成员名称")
        return self

    def search_and_get_result(self, name):
        page = self.search(name).click(loc=contact_page_loc.searchResultList, image_desc="点击搜索后的结果进入成员详情页")
        member_date = member(name=page.get_text(loc=contact_page_loc.nameLocator, image_desc="获取成员详情的名称文本"),
                             depart=page.get_text(loc=contact_page_loc.departLocator, image_desc="获取成员详情的部门文本"))
        return member_date
