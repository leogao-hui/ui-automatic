#_author:leo gao
#encoding:utf-8

import allure
import pytest


@allure.feature('成员管理,删除人员')
@pytest.mark.usefixtures('normal_login')
class TestDeleteUser:

    @allure.story('这是一个测试正常删除用户的case')
    def test_normal_delete_user(self, state_delete_user_management_class):
        '''
        用例描述：删除用户
        :return:
        '''
        state_delete_user_management_class.click_user_delete()
        assert '' == state_delete_user_management_class.assert_delete_user_serial_number()
        assert '' == state_delete_user_management_class.assert_delete_user_name()
        assert '' == state_delete_user_management_class.assert_delete_user_account()

        # 关闭页面
        state_delete_user_management_class.close_web()

    # 登陆的时候不能删除用户 ,需同时登录两个账号，目前不支持

