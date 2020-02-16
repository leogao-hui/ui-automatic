#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from ElementLayer.userManagement.useManagementElement import UserManagementElement


class UserManagementDeleteOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('点击删除')
    def click_user_delete(self):
        self.click(UserManagementElement.first_blank_space)
        self.click(UserManagementElement.delete_user_button)
        self.click(UserManagementElement.delete_user_confirm_button)

    @allure.step('验证序号')
    def assert_delete_user_serial_number(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_serial_number)

    @allure.step('验证新增人员姓名')
    def assert_delete_user_name(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_name)

    @allure.step('验证新增人员账号名')
    def assert_delete_user_account(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_account)

    @allure.step('验证新增人员组织机构')
    def assert_delete_user_organization(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_organization)

    @allure.step('步骤5：关闭页面')
    def close_web(self):
        self.close()