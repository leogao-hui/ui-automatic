# _author:leo gao
# encoding:utf-8

import allure
from Base.base import Base
from elementLayer.deviceManagement.deviceManagementElement import DeviceManagementElement


class DeviceManagementModifyOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('1.点击空格 2.点击修改')
    def click_device_management(self):
        self.use_js_click(DeviceManagementElement.first_blank_space)
        self.use_js_click(DeviceManagementElement.modify_device_button)

    @allure.step('修改设备名称')
    def modify_device_name(self, modify_device_name):
        self.clear(DeviceManagementElement.add_device_name_input)
        self.send_keys(DeviceManagementElement.add_device_name_input, modify_device_name)

    @allure.step('修改设备ip')
    def modify_device_ip(self, modify_device_ip):
        self.clear(DeviceManagementElement.add_device_ip_input)
        self.send_keys(DeviceManagementElement.add_device_ip_input, modify_device_ip)

    @allure.step('修改生产厂家')
    def modify_manufacturer(self, modify_manufacturer):
        self.clear(DeviceManagementElement.modify_manufacturer_input)
        self.send_keys(DeviceManagementElement.modify_manufacturer_input, modify_manufacturer)

    @allure.step('点击修改确定')
    def click_button(self):
        self.use_js_click(DeviceManagementElement.add_device_confirm_button)

    @allure.step('验证设备名称')
    def assert_device_name(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_device_name)

    @allure.step('验证设备ip')
    def assert_device_ip(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_device_ip)

    @allure.step('验证生产厂家')
    def assert_manufacturer(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_bind_manufacturer)

    @allure.step('关闭页面')
    def close_web(self):
        self.close()
