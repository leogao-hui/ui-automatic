#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class UserManagementElement:

    # 用户管理按钮
    user_management_button = (By.XPATH, '//*[text()="用户管理"]')

    # 添加用户按钮
    add_user_button = (By.XPATH, '//*[text()="添加"]')

    # 添加用户编号输入框
    add_user_serial_number_input = (By.XPATH, '//*[@class="adduser-content-main"]/ul/li[1]/input')

    # 添加用户姓名输入框
    add_user_name_input = (By.XPATH, '//*[@class="adduser-content-main"]/ul/li[2]/input')

    # 添加用户账号名输入框
    add_user_account_input = (By.XPATH, '//*[@class="adduser-content-main"]/ul/li[3]/input')

    # 所属组织结构选择框
    belong_to_organization_select_box = (By.XPATH, '//*[@class="adduser-content-main"]/ul/li[5]/input')

    # 总军区
    total_military_area_command = (By.XPATH, '//*[@class="orgstructure-scroll-treebox"]/div/li/div/span/span/span')

    # 添加人员确定按钮
    add_user_confirm_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[1]')

    # 添加人员取消按钮
    add_user_cancel_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[2]')

    # 删除人员确定按钮
    delete_user_confirm_button = (By.XPATH, '')

    # 删除人员取消按钮
    delete_user_cancel_button = (By.XPATH, '')

    # 修改用户按钮
    modify_user_button = (By.XPATH, '//*[text()="修改"]')

    # 删除用户按钮
    delete_user_button = (By.XPATH, '//*[text()="删除"]')

    # 密码重置按钮
    reset_password_button = (By.XPATH, '//*[text()="密码重置"]')

    # 绑定设备
    bind_device_button = (By.XPATH, '//*[text()="绑定设备"]')

    # 未绑定设备位置一
    not_bind_device_one = (By.XPATH, '//div[@class="notBind"]/ul/div/div/div/li/span')

    # 未绑定设备位置二
    not_bind_device_two = (By.XPATH, '//div[@class="notBind"]/ul/div/div/div/li[2]/span')

    # 未绑定设备位置三
    not_bind_device_three = (By.XPATH, '//div[@class="notBind"]/ul/div/div/div/li[3]/span')

    # 未绑定设备位置四
    not_bind_device_four = (By.XPATH, '//div[@class="notBind"]/ul/div/div/div/li[4]/span')

    # 未绑定设备位置五
    not_bind_device_five = (By.XPATH, '//div[@class="notBind"]/ul/div/div/div/li[5]/span')

    # 绑定设备
    bind_device = (By.XPATH, '//div[@class="binded"]/ul/div/div/div')

    # 导出按钮
    export_button = (By.XPATH, '//*[text()="导出"]')

    # 模版下载
    download_template_button = (By.XPATH, '//*[text()="模版下载"]')

    # 导入按钮
    import_button = (By.XPATH, '//*[text()="导入"]')

    # 搜索姓名输入框
    search_name_input = (By.XPATH, '//*[@class="searchul"]/li/input')

    # 搜索账户名输入框
    search_account_input = (By.XPATH, '//*[@class="searchul"]/li[1]/input')

    # 搜索组织机构输入框
    search_organization_input = (By.XPATH, '//*[@class="selli"]/input')

    # 搜索按钮
    search_button = (By.XPATH, '//*[@class="searchbtnBox"]/button[0]')

    # 重置按钮
    reset_button = (By.XPATH, '//*[@class="searchbtnBox"]/button[1]')

    # 第一排空格
    first_blank_space = (By.XPATH, '//*[@class="listData"]/li/span/label/span/span')

    # 第一排序号
    first_row_serial_number = (By.XPATH, '//*[@class="listData"]/li/span[2]')

    # 第一排姓名
    first_row_name = (By.XPATH, '//*[@class="listData"]/li/span[3]')

    # 第一排账号名
    first_row_account = (By.XPATH, '//*[@class="listData"]/li/span[4]')

    # 第一排组织机构
    first_row_organization = (By.XPATH, '//*[@class="listData"]/li/span[5]')

    # 第一排角色
    first_row_role = (By.XPATH, '//*[@class="listData"]/li/span[6]')

    # 第一排绑定设备
    first_row_bind_device = (By.XPATH, '//*[@class="listData"]/li/span[7]')

    # 第一排账号状态
    first_row_account_status = (By.XPATH, '//*[@class="listData"]/li/span[8]')

    # 修改用户时的姓名
    modify_user_name = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[2]/ul/li/input')

    # 修改用户时的账号
    modify_user_account = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[2]/ul/li[2]/input')

    # 修改用户时的所属组织机构
    modify_user_belong_to_organization = (By.XPATH, '//*[@class="adduser-content-main"]/ul/li[3]/input')

    # 修改用户时的确定按钮
    modify_user_confirm_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[1]')

    # 修改用户时的取消按钮
    modify_user_cancel_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[2]')

    # 验证弹框
    assert_bounced = (By.XPATH, '//*[@class="modal"]/div/div/div[2]')

