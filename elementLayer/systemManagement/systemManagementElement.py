#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class SystemManagementElement:

    # 系统管理按钮
    system_manager_button = (By.XPATH, '//*[text()="系统管理"]')

    # 编辑按钮
    edit_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/span[1]')

    # 设备服务器名称输入框
    device_name_input = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/ul/li/input')

    # 设备服务器ip地址输入框
    device_ip_input = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/ul/li[2]/input')

    # 设备服务器端口号输入框
    device_port_input = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/ul/li[3]/input')

    # 打勾按钮
    tick_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/span[3]')

    # 确定按钮
    confirm_button = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div[3]/button[1]')
