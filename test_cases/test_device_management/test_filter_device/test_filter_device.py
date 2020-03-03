#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time
from Data.deviceManagement.add_device import filter_add_device_data


@allure.feature('设备管理,过滤设备')
@pytest.mark.usefixtures('normal_login')
class TestFilterDevice:

    @allure.story('这是一条过滤编号的case')
    def test_filter_serial_number(self, state_add_device_management_class):
        '''
        用例描述：新增4个人员
        :return:
        '''
        for key in filter_add_device_data.filter_add_user_data:
            state_add_device_management_class.click_user_management()
            state_add_device_management_class.add_user(
                key['serial_num'],
                key['name'],
                key['account'])
            state_add_device_management_class.choose_organization()
            time.sleep(1)
            state_add_device_management_class.confirm()
