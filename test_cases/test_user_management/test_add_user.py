#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time
from Data.userManagement import normal_add_user_data, modify_user_name_data


@allure.feature('成员管理')
@pytest.mark.usefixtures('state_add_user_management_class')
@pytest.mark.usefixtures('normal_login')
class TestAddUser:

    @allure.story('这是一个测试正常新增的case')
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
        assert normal_add_user_data.normal_add_user_data['serial_num'] == state_add_user_management_class.\
            assert_add_user_serial_number()
        assert normal_add_user_data.normal_add_user_data['name'] == state_add_user_management_class.assert_add_user_name()
        assert normal_add_user_data.normal_add_user_data['account'] == state_add_user_management_class.\
            assert_add_user_account()

    # @allure.story('这是一个测试修改用户名字账号的case')
    # def test_modify_(self, state_add_user_management_class):
    #     state_add_user_management_class.click_user_management()
    #     state_add_user_management_class.add_user(modify_user_name_data.modify_user_name_data['serial_num'],
    #                                          modify_user_name_data.modify_user_name_data['name'],
    #                                          modify_user_name_data.modify_user_name_data['account'])
    #     state_add_user_management_class.choose_organization()
    #     state_add_user_management_class.confirm()



