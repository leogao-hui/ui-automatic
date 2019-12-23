#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class UserManagementElement:

    # 用户管理按钮
    user_management_button = (By.CLASS_NAME, 'sidebar_title')

    # 添加用户按钮
    add_user_button = (By.XPATH, '//*[@class="usermanage-button"]/button[0]')

    # 修改用户按钮
    modify_user_button = (By.XPATH, '//*[@class="usermanage-button"]/button[1]')

    # 删除用户按钮
    delete_user_button = (By.XPATH, '//*[@class="usermanage-button"]/button[2]')

    # 密码重置按钮
    reset_password_button = (By.XPATH, '//*[@class="usermanage-button"]/button[3]')

    # 绑定设备
    bind_device_button = (By.XPATH, '//*[@class="usermanage-button"]/button[4]')

    # 导出按钮
    export_button = (By.XPATH, '//*[@class="usermanage-button"]/button[5]')

    # 模版下载
    download_template_button = (By.XPATH, '//*[@class="usermanage-button"]/button[6]')

    # 导入按钮
    import_button = (By.XPATH, '//*[@class="usermanage-button"]/div/div/button[0]')

