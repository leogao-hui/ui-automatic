#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class LoginElement:

    # 账号输入框
    account_input_box = (By.CLASS_NAME, 'username')

    # 密码输入框
    password_input_box = (By.XPATH, '//input[@class="password"]')

    # 验证码输入框
    verification_code_input_box = (By.XPATH, '//*[@class="idcode"]/input')

    # 登录按钮
    login_confirm_input_box = (By.CLASS_NAME, 'login-confirm')

    # 验证登录失败
    assert_account_wrong = (By.XPATH, '//*[@class="tips"]/span')

    # 弹框验证
    assert_bounced = (By.XPATH, '//*[@class="frame"]/div[2]')

    # 记住密码
    remember_password_input_box = (By.XPATH, '//*[@class="rememberPwd"]/label/span/span')

    # 原密码输入框
    original_password_input_box = (By.XPATH, '//*[@class="modifypwd adduser"]/div[2]/div[2]/ul/li[2]/input')

    # 新密码输入框
    new_password_input_box = (By.XPATH, '//*[@class="modifypwd adduser"]/div[2]/div[2]/ul/li[3]/input')

    # 确认密码输入框
    confirm_password_input_box = (By.XPATH, '//*[@class="modifypwd adduser"]/div[2]/div[2]/ul/li[4]/input')

    # 确认密码按钮
    confirm_password_button = (By.XPATH, '//*[@class="modifypwd adduser"]/div[2]/div[3]/button[1]')

    # 取消密码按钮
    cancel_password_button = (By.XPATH, '//*[@class="modifypwd adduser"]/div[2]/div[3]/button[2]')

    # 登录账号位置
    login_account_button = (By.XPATH, '//*[@id="app"/div[3]/div/div[3]/span')

    # 注销按钮
    cancellation_button = (By.XPATH, '//*[@class="manage"]/div/div[3]/div/ul/li[4]')

    # 注销确认按钮
    cancellation_confirm_button = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button')

    # 注销取消按钮
    cancellation_cancel_button = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
