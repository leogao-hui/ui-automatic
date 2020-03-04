#_author:leo gao
#encoding:utf-8

import allure
import time
from Base.base import Base
from elementLayer.deviceManagement.deviceManagementElement import DeviceManagementElement


class DeviceManagementDeleteOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('1.点击删除按钮')
    def delete_device(self):
        self.click(DeviceManagementElement.first_blank_space)
        self.click(DeviceManagementElement.delete_device_button)
        self.click(DeviceManagementElement.delete_device_confirm_button)

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



