#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from elementLayer.userManagement.useManagementElement import UserManagementElement


class UserManagementModifyOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('点击修改')
    def click_user_modify(self):
        self.click(UserManagementElement.first_blank_space)
        self.click(UserManagementElement.modify_user_button)

    @allure.step('1.修改姓名2.修改账户名')
    def modify_user(self, name, account):
        self.clear(UserManagementElement.modify_user_name)
        self.send_keys(UserManagementElement.modify_user_name, name)
        self.clear(UserManagementElement.modify_user_account)
        self.send_keys(UserManagementElement.modify_user_account, account)

    @allure.step('点击确定')
    def confirm(self):
        self.click(UserManagementElement.add_user_confirm_button)

    @allure.step('验证新增人员姓名')
    def assert_user_name(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_name)

    @allure.step('验证新增人员账号名')
    def assert_user_account(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_account)

    @allure.step('步骤5：关闭页面')
    def close_web(self):
        self.close()


