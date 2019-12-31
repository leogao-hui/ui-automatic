#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class DeviceManagementElement:

    # 设备管理按钮
    device_management_button = (By.XPATH, '//*[text()="设备管理"]')

    # 添加按钮
    add_device_button = (By.XPATH, '//*[text()="添加"]')

    # 添加设备名称输入框
    add_device_name_input = (By.XPATH, '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li/input')

    # 添加设备ip输入框
    add_device_ip_input = (By.XPATH, '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[2]/input')

    # 添加设备类型下拉框
    add_device_type_drop_down_box = (By.XPATH,
                                     '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input')

    # 解码器
    decoder = (By.XPATH, '//*[class="el-select-dropdown el-popper playersel"]/div/div/ul/li[2]/span')

    # # 编码器
    # encoder = (By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span')
    encoder = (By.XPATH, '//*[text()="编码器"]')

    # 所属组织机构下拉框
    belong_to_organization_drop_down_box = (By.XPATH, '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[5]/input')

    # 总军区
    total_military_area_command = (By.XPATH, '//*[@class="orgstructure-scroll-treebox"]/div/li/div/span/span/span')

    # 生产厂家
    manufacturer_input = (By.XPATH, '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[6]/input')

    # 修改生产厂家
    modify_manufacturer_input = (By.XPATH, '//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[5]/input')

    # 添加设备确定按钮
    add_device_confirm_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[1]')

    # 添加设备取消按钮
    add_device_cancel_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[3]/button[2]')

    # 修改设备按钮
    modify_device_button = (By.XPATH, '//*[text()="修改"]')

    # 删除设备按钮
    delete_device_button = (By.XPATH, '//*[text()="删除"]')

    # 查看设备
    view_device_button = (By.XPATH, '//*[text()="查看"]')

    # 导入
    import_button = (By.XPATH, '//*[text()="导入"]')

    # 导出
    export_button = (By.XPATH, '//*[text()="导出"]')

    # 模版下载
    download_template_button = (By.XPATH, '//*[text()="模版下载"]')

    # 第一排空格
    first_blank_space = (By.XPATH, '//*[@class="listData"]/li/span/label/span')

    # 第一排序号
    first_row_serial_number = (By.XPATH, '//*[@class="listData"]/li/span[2]')

    # 第一排设备名称
    first_row_device_name = (By.XPATH, '//*[@class="listData"]/li/span[3]')

    # 第一排组织结构
    first_row_organization = (By.XPATH, '//*[@class="listData"]/li/span[4]')

    # 第一排设备ip
    first_row_device_ip = (By.XPATH, '//*[@class="listData"]/li/span[5]')

    # 第一排设备类型
    first_row_device_type = (By.XPATH, '//*[@class="listData"]/li/span[6]')

    # 第一排生产厂家
    first_row_bind_manufacturer = (By.XPATH, '//*[@class="listData"]/li/span[7]')

    # 第一排是否绑定
    first_row_is_bind = (By.XPATH, '//*[@class="listData"]/li/span[8]')

    # 第一排设备状态
    first_row_device_status = (By.XPATH, '//*[@class="listData"]/li/span[9]')

    # 添加报错信息
    add_error_information = (By.XPATH, '//*[@class="modal"]/transition/div/transition/div/div[2]')



