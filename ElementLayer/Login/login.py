#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class LoginElement:

    # 账号输入框
    account_input_box = (By.CLASS_NAME, 'username')

    # 密码输入框
    password_input_box = (By.CLASS_NAME, 'password')

    # 验证码输入框
    verification_code_input_box = (By.XPATH, '//*[@class="idcode"]/input')

    # 登录按钮
    login_confirm_input_box = (By.CLASS_NAME, 'login-confirm')


