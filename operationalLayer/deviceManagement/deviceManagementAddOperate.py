#_author:leo gao
#encoding:utf-8

import allure
import time
from Base.base import Base
from elementLayer.deviceManagement.deviceManagementElement import DeviceManagementElement


class DeviceManagementAddOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('1.点击设备管理 2.点击新增按钮')
    def click_device_management(self):
        self.click(DeviceManagementElement.device_management_button)
        self.click(DeviceManagementElement.add_device_button)

    @allure.step('3.输入设备名称 4.输入设备ip')
    def input_device_name_ip(self, device_name, device_ip):
        self.send_keys(DeviceManagementElement.add_device_name_input, device_name)
        self.send_keys(DeviceManagementElement.add_device_ip_input, device_ip)

    @allure.step('选择设备类型')
    def choose_device_type(self):
        self.use_js_click(DeviceManagementElement.encoder)

    @allure.step('选择所属机构，输入生产厂家, 点击确定')
    def choose_organization_manufacturer(self, manufacturer):
        self.use_js_click(DeviceManagementElement.belong_to_organization_drop_down_box)
        self.use_js_click(DeviceManagementElement.total_military_area_command)
        self.send_keys(DeviceManagementElement.manufacturer_input, manufacturer)
        self.click(DeviceManagementElement.add_device_confirm_button)

    @allure.step('选择所属机构，输入生产厂家')
    def choose_organization_manufacturer_extra(self, manufacturer):
        self.use_js_click(DeviceManagementElement.belong_to_organization_drop_down_box)
        self.use_js_click(DeviceManagementElement.total_military_area_command)
        self.send_keys(DeviceManagementElement.manufacturer_input, manufacturer)

    @allure.step('点击确定')
    def confirm(self):
        self.click(DeviceManagementElement.add_device_confirm_button)

    @allure.step('关闭页面')
    def close_web(self):
        self.close()

    @allure.step('验证序号')
    def assert_serial_number(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_serial_number)

    @allure.step('验证设备名称')
    def assert_device_name(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_device_name)

    @allure.step('验证设备ip')
    def assert_device_ip(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_device_ip)

    @allure.step('验证设备类型')
    def assert_device_type(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_device_type)

    @allure.step('验证生产厂家')
    def assert_manufacturer(self):
        return self.get_txt_in_tag(DeviceManagementElement.first_row_bind_manufacturer)

    @allure.step('报错信息')
    def assert_error_information(self):
        self.get_txt_in_tag(DeviceManagementElement.add_error_information)

    @allure.step('获取弹窗报错信息')
    def validate_bounced_error_information(self):
        return self.get_txt_in_tag(DeviceManagementElement.assert_bounced)


