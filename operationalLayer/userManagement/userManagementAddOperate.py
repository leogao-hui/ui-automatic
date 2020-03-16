#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from elementLayer.userManagement.useManagementElement import UserManagementElement


class UserManagementAddOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('点击用户管理')
    def click_user_management(self):
        self.click(UserManagementElement.user_management_button)

    @allure.step('1.点击添加2.输入编号3.输入姓名4.输入账号')
    def add_user(self, serial_number, name, account):
        self.click(UserManagementElement.add_user_button)
        self.send_keys(UserManagementElement.add_user_serial_number_input, serial_number)
        self.send_keys(UserManagementElement.add_user_name_input, name)
        self.send_keys(UserManagementElement.add_user_account_input, account)

    @allure.step('选择所属机构')
    def choose_organization(self):
        self.use_js_click(UserManagementElement.belong_to_organization_select_box)
        self.use_js_click(UserManagementElement.total_military_area_command)

    @allure.step('点击确定')
    def confirm(self):
        self.click(UserManagementElement.add_user_confirm_button)

    @allure.step('点击空格修改')
    def click_space(self):
        self.click(UserManagementElement.export_button)
        self.click(UserManagementElement.modify_user_button)

    @allure.step('修改姓名')
    def modify_name(self, name):
        self.clear(UserManagementElement.modify_user_name)
        self.send_keys(UserManagementElement.modify_user_name, name)

    @allure.step('修改账号')
    def modify_account(self, account):
        self.clear(UserManagementElement.modify_user_account)
        self.send_keys(UserManagementElement.modify_user_account, account)

    @allure.step('验证序号')
    def assert_add_user_serial_number(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_serial_number)

    @allure.step('验证新增人员姓名')
    def assert_add_user_name(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_name)

    @allure.step('验证新增人员账号名')
    def assert_add_user_account(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_account)

    @allure.step('验证新增人员组织机构')
    def assert_add_user_organization(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_organization)

    @allure.step('验证新增人员角色')
    def assert_add_user_role(self):
        return self.get_txt_in_tag(UserManagementElement.first_row_role)

    @allure.step('步骤5：关闭页面')
    def close_web(self):
        self.close()

    @allure.step('报错信息')
    def assert_error_information(self):
        self.get_txt_in_tag()

    @allure.step('获取弹窗报错信息')
    def validate_bounced_error_information(self):
        return self.get_txt_in_tag(UserManagementElement.assert_bounced)







