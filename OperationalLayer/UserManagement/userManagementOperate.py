#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from ElementLayer.userManagement.useManagement import UserManagementElement


class UserManagementOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('1.点击添加2.输入编号3.输入姓名4.输入账号')
    def add_user(self, serial_number, name, account):
        self.click(UserManagementElement.add_user_button)
        self.send_keys(UserManagementElement.add_user_serial_number_input, serial_number)
        self.send_keys(UserManagementElement.add_user_name_input, name)
        self.send_keys(UserManagementElement.add_user_account_input, account)

    @allure.step('选择所属机构')
    def choose_organization(self):
        self.click(UserManagementElement.belong_to_organization_select_box)
        self.click(UserManagementElement.total_military_area_command)

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






