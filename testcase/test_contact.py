from common.log_handle import log
from page.app_start import App
from page.base_page import BasePage


class TestAddMember:
    default = App().start()
    member = default.into_contact_page().add_member("python测试2", "13321123221").search_and_get_result("python测试")
    try:
        assert member.name == "python测试2"
        assert member.depart == "研发部"
    except Exception as e:
        # 截图
        log.exception("正常添加成员失败")
        default.screenshot("添加成员失败")
        raise e
    else:
        log.info("正常添加成员成功")
