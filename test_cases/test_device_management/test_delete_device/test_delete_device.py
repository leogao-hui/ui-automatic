#_author:leo gao
#encoding:utf-8

import pytest
import allure
import time
from Data.deviceManagement.delete_device import device_bind_user_not_delete_data


@allure.feature('设备管理，删除设备')
@pytest.mark.usefixtures('normal_login')
class TestDeleteDevice:

    @allure.story('这是一个测试正常删除设备的case')
    def test_normal_delete_device(self, state_delete_device_management_class):
        '''
        用例描述：删除用户
        :return:
        '''
        state_delete_device_management_class.delete_device()
        assert '' == state_delete_device_management_class.assert_delete_user_serial_number()
        assert '' == state_delete_device_management_class.assert_delete_user_name()
        assert '' == state_delete_device_management_class.assert_delete_user_account()

        # 关闭页面
        state_delete_device_management_class.close_web()

    # 设备被用户绑定不能删除
    @allure.story('这是一个测试设备被用户绑定不能删除的case')
    def test_device_bind_user_not_delete(self, state_add_user_management_class):
        '''
        设备被用户绑定时不能删除
        '''
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(device_bind_user_not_delete_data.add_user_data['serial_num'],
                                                 device_bind_user_not_delete_data.add_user_data['name'],
                                                 device_bind_user_not_delete_data.add_user_data['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()

