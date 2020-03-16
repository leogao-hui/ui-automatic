#_author:leo gao
#encoding:utf-8


import allure
from Base.base import Base
from elementLayer.Login.loginElement import LoginElement


class LoginOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    # 获取登录界面url
    @allure.step('到达登录页面')
    def get_login_url(self):
        self.get_url()

    # 输入账号，密码，验证码
    @allure.step('输入账号，密码，验证码')
    def input_account(self, account, password, verification_code):
        self.send_keys(LoginElement.account_input_box, account)
        self.send_keys(LoginElement.password_input_box, password)
        self.send_keys(LoginElement.verification_code_input_box, verification_code)

    @allure.step('点击登录按钮')
    # 点击确认登录按钮
    def confirm_login_button(self):
        self.use_js_click(LoginElement.login_confirm_input_box)

    @allure.step('验证跳转页面')
    def validate_jump_page(self):
        return self.receive_current_url()

    @allure.step('获取页面handle')
    def receive_handle(self):
        return self.receive_handle()

    @allure.step('跳转页面')
    def switch_handle(self, data):
        return self.switch_handle(data)

    @allure.step('获取报错信息')
    def validate_account_not_exist(self):
        return self.get_txt_in_tag(LoginElement.assert_account_wrong)

    @allure.step('获取弹窗报错信息')
    def validate_bounced_error_information(self):
        return self.get_txt_in_tag(LoginElement.assert_bounced)

    @allure.step('点击记住密码')
    def click_remember_password(self):
        return self.use_js_click(LoginElement.remember_password_input_box)

    @allure.step('关闭页面')
    def close_web(self):
        self.close()

    @allure.step('关闭页面')
    def quit_web(self):
        self.quit()

    @allure.step('重置密码')
    def reset_password(self, old_pwd, new_pwd, confirm_pwd):
        self.send_keys(LoginElement.original_password_input_box, old_pwd)
        self.send_keys(LoginElement.new_password_input_box, new_pwd)
        self.send_keys(LoginElement.confirm_password_input_box, confirm_pwd)
        self.use_js_click(LoginElement.confirm_password_button)

    @allure.step('清空账户数据')
    def clear_data(self):
        self.mandatory_clear(LoginElement.account_input_box)

    @allure.step('注销账户')
    def cancellation_account(self):
        self.click(LoginElement.login_account_button)
        self.click(LoginElement.cancellation_button)
        self.click(LoginElement.cancellation_confirm_button)
