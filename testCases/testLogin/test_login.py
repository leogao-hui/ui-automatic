#_author:leo gao
#encoding:utf-8


import allure
from Data.Login import noraml_login_data, abnormal_login_data
from testCases.conftest import state_login_class


@allure.feature('登录')
class TestSearchPage:

    @allure.story('这是一个测试正常登录的case')
    def test_normal_login(self):
        '''
        用例描述：输入正确管理员账号，正确密码，验证码（随便），正常登录
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                        noraml_login_data.verification_code)
        state_login_class.confirm_login_button()

    @allure.story('这是一个测试账号错误登录的case')
    def test_account_wrong_login(self):
        '''
        用例描述：输入错误管理员账号，正确密码，验证码（随便），登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(abnormal_login_data.account, abnormal_login_data.password,
                                        abnormal_login_data.verification_code)
        state_login_class.confirm_login_button()
