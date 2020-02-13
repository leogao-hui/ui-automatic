# _author:leo gao
# encoding:utf-8

import allure
import pytest
import time
from Data.userManagement.add_user import normal_add_user_data, serial_number_input_empty_add_user_data, \
    name_input_empty_add_user_data, account_input_empty_add_user_data, organization_empty_add_user_data, \
    serial_number_check_again_add_user_data, name_check_again_add_user_data, account_check_again_add_user_data, \
    filter_add_user_data


@allure.feature('成员管理,新增人员')
@pytest.mark.usefixtures('normal_login')
class TestAddUser:

    @allure.story('这是一个测试正常新增用户的case')
    def test_normal_add_user(self, state_add_user_management_class):
        '''
        用例描述：输入编号，姓名，账号名，选择所属结构，正常新增用户
        :return:
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(normal_add_user_data.normal_add_user_data['serial_num'],
                                                 normal_add_user_data.normal_add_user_data['name'],
                                                 normal_add_user_data.normal_add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        assert normal_add_user_data.normal_add_user_data['serial_num'] == state_add_user_management_class. \
            assert_add_user_serial_number()
        assert normal_add_user_data.normal_add_user_data[
                   'name'] == state_add_user_management_class.assert_add_user_name()
        assert normal_add_user_data.normal_add_user_data['account'] == state_add_user_management_class. \
            assert_add_user_account()
        # 关闭页面
        state_add_user_management_class.close_web()

    @allure.story('这是一个测试编号输入框为空的case')
    def test_serial_number_input_empty(self, state_add_user_management_class):
        '''
        用例描述：输入，姓名，账号名，选择所属结构，正常新增用户
        :return:
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            serial_number_input_empty_add_user_data.serial_number_input_empty_add_user_data['serial_num'],
            serial_number_input_empty_add_user_data.serial_number_input_empty_add_user_data['name'],
            serial_number_input_empty_add_user_data.serial_number_input_empty_add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试姓名输入框为空的case')
    def test_name_input_empty(self, state_add_user_management_class):
        '''
        用例描述：输入编号，账号名，选择所属结构，正常新增用户
        :return:
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            name_input_empty_add_user_data.name_input_empty_add_user_data['serial_num'],
            name_input_empty_add_user_data.name_input_empty_add_user_data['name'],
            name_input_empty_add_user_data.name_input_empty_add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试账户名输入框为空的case')
    def test_account_input_empty(self, state_add_user_management_class):
        '''
        用例描述：输入编号，姓名，选择所属结构，正常新增用户
        :return:
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            account_input_empty_add_user_data.account_input_empty_add_user_data['serial_num'],
            account_input_empty_add_user_data.account_input_empty_add_user_data['name'],
            account_input_empty_add_user_data.account_input_empty_add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试所属机构为空的case')
    def test_organization_input_empty(self, state_add_user_management_class):
        '''
        用例描述：输入编号，姓名，账号，正常新增用户
        :return:
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            organization_empty_add_user_data.organization_empty_add_user_data['serial_num'],
            organization_empty_add_user_data.organization_empty_add_user_data['name'],
            organization_empty_add_user_data.organization_empty_add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试编号验重的case')
    def test_serial_number_check_again(self, state_add_user_management_class):
        '''
        用例描述：新增一个编号为1的人员，再新增一个编号为1的人员
        :return:
        '''
        # 新增第一个成员
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_one['serial_num'],
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_one['name'],
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_one['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 新增第二个
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_two['serial_num'],
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_two['name'],
            serial_number_check_again_add_user_data.serial_number_check_again_add_user_data_two['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试姓名验重的case')
    def test_name_check_again(self, state_add_user_management_class):
        '''
        用例描述：新增一个姓名为1的人员，再新增一个姓名为1的人员
        :return:
        '''
        # 新增第一个成员
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            name_check_again_add_user_data.name_check_again_add_user_data_one['serial_num'],
            name_check_again_add_user_data.name_check_again_add_user_data_one['name'],
            name_check_again_add_user_data.name_check_again_add_user_data_one['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 新增第二个
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            name_check_again_add_user_data.name_check_again_add_user_data_two['serial_num'],
            name_check_again_add_user_data.name_check_again_add_user_data_two['name'],
            name_check_again_add_user_data.name_check_again_add_user_data_two['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一个测试账户名验重的case')
    def test_account_check_again(self, state_add_user_management_class):
        '''
        用例描述：新增一个账户为1的人员，再新增一个账户为1的人员
        :return:
        '''
        # 新增第一个成员
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            account_check_again_add_user_data.name_check_again_add_user_data_one['serial_num'],
            account_check_again_add_user_data.name_check_again_add_user_data_one['name'],
            account_check_again_add_user_data.name_check_again_add_user_data_one['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 新增第二个
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(
            account_check_again_add_user_data.name_check_again_add_user_data_two['serial_num'],
            account_check_again_add_user_data.name_check_again_add_user_data_two['name'],
            account_check_again_add_user_data.name_check_again_add_user_data_two['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        # 断言

    @allure.story('这是一条过滤编号的case')
    def test_filter_serial_number(self, state_add_user_management_class):
        '''
        用例描述：新增4个人员
        :return:
        '''
        for key in filter_add_user_data.filter_add_user_data:
            state_add_user_management_class.click_user_management()
            state_add_user_management_class.add_user(
                key['serial_num'],
                key['name'],
                key['account'])
            state_add_user_management_class.choose_organization()
            time.sleep(1)
            state_add_user_management_class.confirm()
            # 断言

    @allure.story('这是一条过滤姓名的case')
    def test_filter_name(self, state_add_user_management_class):
        '''
        用例描述：新增4个人员
        :return:
        '''
        for key in filter_add_user_data.filter_add_user_data:
            state_add_user_management_class.click_user_management()
            state_add_user_management_class.add_user(
                key['serial_num'],
                key['name'],
                key['account'])
            state_add_user_management_class.choose_organization()
            time.sleep(1)
            state_add_user_management_class.confirm()
            # 断言

    @allure.story('这是一条过滤账号的case')
    def test_filter_account(self, state_add_user_management_class):
        '''
        用例描述：新增4个人员
        :return:
        '''
        for key in filter_add_user_data.filter_add_user_data:
            state_add_user_management_class.click_user_management()
            state_add_user_management_class.add_user(
                key['serial_num'],
                key['name'],
                key['account'])
            state_add_user_management_class.choose_organization()
            time.sleep(1)
            state_add_user_management_class.confirm()
            # 断言
