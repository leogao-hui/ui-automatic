#_author:leo gao
#encoding:utf-8

import allure
import time
import pytest
from Data.userManagement.normal_add_user import normal_add_user_data


@allure.feature('成员管理')
@pytest.mark.usefixtures('state_user_management_class')
@pytest.mark.usefixtures('normal_login')
class TestAddUser:

    @allure.story('这是一个测试正常新增的case')
    def test_normal_login(self, state_user_management_class):
        '''
        用例描述：输入编号，姓名，账号名，选择所属结构，正常新增用户
        :return:
        '''
        state_user_management_class.add_user(normal_add_user_data['serial_num'],
                                             normal_add_user_data['name'], normal_add_user_data['account'])
        state_user_management_class.choose_organization()
        state_user_management_class.confirm()


