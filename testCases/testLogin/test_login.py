#_author:leo gao
#encoding:utf-8


import allure
import time
import pytest
from Data.Login import noraml_login_data, abnormal_login_data


@allure.feature('登录')
@pytest.mark.usefixtures('state_login_class')
class TestSearchPage:

    @allure.story('这是一个测试正常登录的case')
    def test_normal_login(self, state_login_class):
        '''
        用例描述：输入正确管理员账号，正确密码，验证码（随便）正常登录
        :return:
        '''

        state_login_class.get_login_url()
        state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                        noraml_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert state_login_class.validate_jump_page() == 'http://10.66.8.200:8088/#/manage'
        state_login_class.close_web()

    @allure.story('这是一个测试账号错误登录的case')
    def test_account_wrong_login(self, state_login_class):
        '''
        用例描述：输入错误管理员账号，正确密码，验证码（随便），登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(abnormal_login_data.account, abnormal_login_data.password,
                                        abnormal_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert '登录信息有误，请确认后重新登录' in state_login_class.validate_account_not_exist()
        state_login_class.close_web()
