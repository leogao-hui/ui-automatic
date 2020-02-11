#_author:leo gao
#encoding:utf-8


import allure
from Base.base import Base
from ElementLayer.Login.loginElement import LoginElement


class LoginOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    # 获取登录界面url
    @allure.step('步骤1：到达登录页面')
    def get_login_url(self):
        self.get_url()

    # 输入账号，密码，验证码
    @allure.step('步骤2：输入账号，密码，验证码')
    def input_account(self, account, password, verification_code):
        self.send_keys(LoginElement.account_input_box, account)
        self.send_keys(LoginElement.password_input_box, password)
        self.send_keys(LoginElement.verification_code_input_box, verification_code)

    @allure.step('步骤3：点击登录按钮')
    # 点击确认登录按钮
    def confirm_login_button(self):
        self.click(LoginElement.login_confirm_input_box)

    @allure.step('步骤4：验证跳转页面')
    def validate_jump_page(self):
        return self.receive_current_url()

    @allure.step('步骤5：获取页面handle')
    def receive_handle(self):
        return self.receive_handle()

    @allure.step('步骤6：跳转页面')
    def switch_handle(self, data):
        return self.switch_handle(data)

    @allure.step('步骤4：获取账号不存在报错信息')
    def validate_account_not_exist(self):
        return self.get_txt_in_tag(LoginElement.assert_account_wrong)

    @allure.step('步骤5：关闭页面')
    def close_web(self):
        self.close()


