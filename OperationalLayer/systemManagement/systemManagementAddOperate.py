#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from ElementLayer.systemManagement.systemManagementElement import SystemManagementElement


class SystemManagementAddOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('新增设备服务器')
    def add_device_server(self, name, ip, port):
        self.click(SystemManagementElement.system_manager_button)
        self.click(SystemManagementElement.edit_button)
        self.send_keys(SystemManagementElement.device_name_input, name)
        self.send_keys(SystemManagementElement.device_ip_input, ip)
        self.send_keys(SystemManagementElement.device_port_input, port)
        self.click(SystemManagementElement.tick_button)
        self.click(SystemManagementElement.confirm_button)

