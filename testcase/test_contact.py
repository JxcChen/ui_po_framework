from common.log_handle import log
from page.app import App
import pytest


class TestAddMember:
    def setup(self):
        self.main_page = App().start().main()

    def test_add_contact(self):
        self.main_page.into_contact().add_member("chenjinxuan","123456666n")