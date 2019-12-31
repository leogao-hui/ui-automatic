# _author:leo gao
# encoding:utf-8

import allure
import pytest
import time
from Data.deviceManagement.modify_device import normal_modify_device_data


@allure.feature('修改设备')
@pytest.mark.usefixtures('add_device_fixture')
@pytest.mark.usefixtures('normal_login')
class TestModifyDevice:

    @allure.story('这是一个修改设备名字的case')
    def test_modify_device_name(self, state_modify_device_management_class):
        state_modify_device_management_class.click_device_management()
        state_modify_device_management_class.modify_device_name(normal_modify_device_data.
                                                                normal_modify_device_data.get('modify_device_name'))
        state_modify_device_management_class.click_button()

        time.sleep(1)
        assert normal_modify_device_data.normal_modify_device_data.get('modify_device_name') == \
               state_modify_device_management_class.assert_device_name()

        # 关闭页面
        state_modify_device_management_class.close_web()

    @allure.story('这是一个修改设备ip的case')
    def test_modify_device_ip(self, state_modify_device_management_class):
        state_modify_device_management_class.click_device_management()
        state_modify_device_management_class.modify_device_ip(normal_modify_device_data.
                                                              normal_modify_device_data.get('modify_device_ip'))

        state_modify_device_management_class.click_button()

        time.sleep(1)
        assert normal_modify_device_data.normal_modify_device_data.get('modify_device_ip') == \
               state_modify_device_management_class.assert_device_ip()

        # 关闭页面
        state_modify_device_management_class.close_web()

    @allure.story('这是一个修改设备生产厂家的case')
    def test_modify_manufacturer(self, state_modify_device_management_class):
        state_modify_device_management_class.click_device_management()
        state_modify_device_management_class.modify_manufacturer(normal_modify_device_data.
                                                              normal_modify_device_data.get('modify_manufacturer'))

        state_modify_device_management_class.click_button()
        time.sleep(1)

        assert normal_modify_device_data.normal_modify_device_data.get('modify_manufacturer') == \
               state_modify_device_management_class.assert_manufacturer()

        # 关闭页面
        state_modify_device_management_class.close_web()


