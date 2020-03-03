#_author:leo gao
#encoding:utf-8


import allure
import time
import pytest
from Data.Login import noraml_login_data, wrong_account_login_data, empty_account_login_data, empty_password_login_data,\
    wrong_password_login_data, manage_login_data, staff_login_data, remember_password_login_data, \
    wrong_password_five_times_login_data, account_locked_login_data, two_times_login_data, \
    different_account_on_same_computer_data


@allure.feature('登录')
@pytest.mark.usefixtures('state_login_class')
class TestLogin:

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
        assert 'http://10.66.8.200:8088/#/manage' == state_login_class.validate_jump_page()
        state_login_class.close_web()

    @allure.story('这是一个测试账号输入框为空的case')
    def test_account_input_empty(self, state_login_class):
        '''
        用例描述：测试账号不输入内容，输入正确的密码，登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(empty_account_login_data.account, empty_account_login_data.password,
                                        empty_account_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        print()
        assert '登录信息有误!' in state_login_class.validate_account_not_exist()
        state_login_class.close_web()

    @allure.story('这是一个测试密码输入框为空的case')
    def test_password_input_empty(self, state_login_class):
        '''
        用例描述：输入正确的账号，密码输入框为空，登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(empty_password_login_data.account, empty_password_login_data.password,
                                        empty_password_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert '登录密码不能为空!' in state_login_class.validate_account_not_exist()
        state_login_class.close_web()

    @allure.story('这是一个测试账号错误登录的case')
    def test_account_wrong_login(self, state_login_class):
        '''
        用例描述：输入错误管理员账号，正确密码，验证码（随便），登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(wrong_account_login_data.account, wrong_account_login_data.password,
                                        wrong_account_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert '登录信息有误，请确认后重新登录' in state_login_class.validate_bounced_error_information()
        state_login_class.close_web()

    @allure.story('这是一个测试密码错误的case')
    def test_wrong_password(self, state_login_class):
        '''
        用例描述：输入正确的账号，输入错误的密码，登录报错
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(wrong_password_login_data.account, wrong_password_login_data.password,
                                        wrong_password_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert '密码错误1次,剩余次数4次!' in state_login_class.validate_account_not_exist()
        state_login_class.close_web()

    @allure.story('这是一个测试管理人员跳转到管理页面的case')
    def test_manage_login(self, state_login_class):
        '''
        用例描述：管理人员登录界面
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                        noraml_login_data.verification_code)
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert 'http://10.66.8.200:8088/#/manage' == state_login_class.validate_jump_page()
        state_login_class.close_web()

    @allure.story('这是一个测试参谋人员跳转到音视频页面的case')
    def test_staff_login(self, state_login_class, state_add_user_management_class):
        '''
        用例描述：参谋人员登录界面
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(staff_login_data.admin_account, staff_login_data.admin_password,
                                        staff_login_data.admin_verification_code)
        state_login_class.confirm_login_button()
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(staff_login_data.add_staff_data['serial_num'],
                                                 staff_login_data.add_staff_data['name'],
                                                 staff_login_data.add_staff_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()

        # 重置密码
        state_login_class.get_login_url()
        state_login_class.input_account(staff_login_data.login_staff_data['staff_account'],
                                        staff_login_data.login_staff_data['staff_password'],
                                        staff_login_data.login_staff_data['staff_verification_code'])
        state_login_class.confirm_login_button()
        state_login_class.reset_password(staff_login_data.reset_password_data['old_pwd'],
                                         staff_login_data.reset_password_data['new_pwd'],
                                         staff_login_data.reset_password_data['confirm_pwd'])
        # 使用新账号登录
        state_login_class.input_account(staff_login_data.new_login_data['staff_account'],
                                        staff_login_data.new_login_data['staff_password'],
                                        staff_login_data.new_login_data['staff_verification_code'])
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert 'http://10.66.8.200:8088/#/spzhsystem/spjk' == state_login_class.validate_jump_page()
        state_login_class.close_web()

    @allure.story('这是一条测试记住密码的case')
    def test_remember_password(self, state_login_class):
        '''
        用例描述：输入用户名，输入密码，点击记住密码，正常登录
        :return:
        '''
        state_login_class.get_login_url()
        state_login_class.input_account(remember_password_login_data.account, remember_password_login_data.password,
                                        remember_password_login_data.verification_code)
        # 点击记住密码
        state_login_class.confirm_login_button()
        time.sleep(1)
        assert 'http://10.66.8.200:8088/#/manage' == state_login_class.validate_jump_page()
        state_login_class.close_web()

    # @allure.story('这是一条测试密码输错5次的case')
    # def test_wrong_password_five_times(self, state_login_class):
    #     '''
    #    用例描述：输入正确用户名，输入错误密码5次
    #    :return:
    #    '''
    #     state_login_class.get_login_url()
    #     state_login_class.input_account(wrong_password_five_times_login_data.account,
    #                                     wrong_password_five_times_login_data.password,
    #                                     wrong_password_five_times_login_data.verification_code)
    #     state_login_class.confirm_login_button()
    #     for i in range(0, 3):
    #         state_login_class.input_account('', '', '')
    #         state_login_class.confirm_login_button()
    #
    #     time.sleep(1)
    #     assert '密码错误4次,剩余次数1次!' in state_login_class.validate_account_not_exist()
    #     state_login_class.close_web()

    @allure.story('这是一条测试账号被锁定的case')
    def test_account_locked(self, state_login_class):
        '''
       用例描述：输入正确用户名，输入错误密码5次，账号被锁定
       :return:
       '''
        state_login_class.get_login_url()
        state_login_class.input_account(account_locked_login_data.account, account_locked_login_data.password,
                                        account_locked_login_data.verification_code)
        state_login_class.confirm_login_button()
        for i in range(0, 4):
            state_login_class.input_account('', '', '')
            state_login_class.confirm_login_button()
        time.sleep(1)

        assert '您已5次输入密码错误,账户被锁定,请5分钟后再进行登录操作' in state_login_class.validate_bounced_error_information()
        state_login_class.close_web()

    # @allure.story('这是一条测试不同用户在同一台电脑上登陆的case')
    # def test_different_account_on_same_computer(self, state_login_class, state_add_user_management_class):
    #     '''
    #    用例描述：正常登录一个用户，再登录其他用户
    #    :return:
    #    '''
    #     state_login_class.get_login_url()
    #     state_login_class.input_account(different_account_on_same_computer_data.admin_account,
    #                                     different_account_on_same_computer_data.admin_password,
    #                                     different_account_on_same_computer_data.admin_verification_code)
    #     state_login_class.confirm_login_button()
    #     state_add_user_management_class.click_user_management()
    #     state_add_user_management_class.add_user(staff_login_data.normal_add_user_data['serial_num'],
    #                                              staff_login_data.normal_add_user_data['name'],
    #                                              staff_login_data.normal_add_user_data['account'])
    #     state_add_user_management_class.choose_organization()
    #     time.sleep(1)
    #     state_add_user_management_class.confirm()
    #     state_login_class.get_login_url()
    #     state_login_class.input_account(different_account_on_same_computer_data.staff_account,
    #                                     different_account_on_same_computer_data.staff_password,
    #                                     different_account_on_same_computer_data.staff_verification_code)
    #     state_login_class.confirm_login_button()
    #     # 重置密码




