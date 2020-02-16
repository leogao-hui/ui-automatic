# _author:leo gao
# encoding:utf-8

import allure
import pytest
import time
from Data.userManagement.modify_user import modify_user_name_account_data


@allure.feature('成员管理,修改人员')
@pytest.mark.usefixtures('add_user')
@pytest.mark.usefixtures('normal_login')
class TestModifyUser:

    @allure.story('这是一个修改人员名字，账号的case')
    def test_modify_user(self, state_modify_user_management_class):
        '''
        用例描述：修改用户姓名，账号正常修改
        :return:
        '''
        time.sleep(2)
        state_modify_user_management_class.click_user_modify()
        state_modify_user_management_class.modify_user(
            modify_user_name_account_data.modify_user_name_data.get('modify_name'),
            modify_user_name_account_data.modify_user_name_data.get('modify_account'))
        state_modify_user_management_class.confirm()
        time.sleep(1)
        assert modify_user_name_account_data.modify_user_name_data.get(
            'modify_name') == state_modify_user_management_class.assert_user_name()
        assert modify_user_name_account_data.modify_user_name_data.get(
            'modify_account') == state_modify_user_management_class.assert_user_account()
        # 关闭页面
        state_modify_user_management_class.close_web()

    @allure.story('这是一个修改人员名字，账号的case')
    def test_modify_user(self, state_modify_user_management_class):
        '''
        用例描述：修改用户姓名，正常修改
        :return:
        '''
        time.sleep(2)
        state_modify_user_management_class.click_user_modify()
        state_modify_user_management_class.modify_user(
            modify_user_name_account_data.modify_user_name_data.get('modify_name'),
            modify_user_name_account_data.modify_user_name_data.get(
                'modify_account'))
        state_modify_user_management_class.confirm()
        time.sleep(1)
        assert modify_user_name_account_data.modify_user_name_data.get(
            'modify_name') == state_modify_user_management_class.assert_user_name()
        assert modify_user_name_account_data.modify_user_name_data.get(
            'modify_account') == state_modify_user_management_class.assert_user_account()
        # 关闭页面
        state_modify_user_management_class.close_web()
