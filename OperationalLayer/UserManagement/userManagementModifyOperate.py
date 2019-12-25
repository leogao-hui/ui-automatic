#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from ElementLayer.userManagement.useManagementElement import UserManagementElement


class UserManagementModifyOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('点击修改')
    def click_user_management(self):
        self.click(UserManagementElement.first_blank_space)
        self.click(UserManagementElement.modify_user_button)

    @allure.step('1.修改姓名2.修改账户名')
    def add_user(self, name, account):
        self.clear(UserManagementElement.modify_user_name)
        self.send_keys(UserManagementElement.modify_user_name, name)
        self.clear(UserManagementElement.modify_user_account)
        self.send_keys(UserManagementElement.modify_user_account, account)

    @allure.step('点击确定')
    def confirm(self):
        self.click(UserManagementElement.add_user_confirm_button)

