#_author:leo gao
#encoding:utf-8

import pytest
import allure


@allure.feature('设备管理，删除设备')
@pytest.mark.usefixtures('normal_login')
class TestDeleteDevice:

    @allure.story('这是一个测试正常删除用户的case')
    def test_normal_delete_device(self, state_delete_device_management_class):
        '''
        用例描述：删除用户
        :return:
        '''
        state_delete_device_management_class.click_user_delete()
        assert '' == state_delete_device_management_class.assert_delete_user_serial_number()
        assert '' == state_delete_device_management_class.assert_delete_user_name()
        assert '' == state_delete_device_management_class.assert_delete_user_account()

        # 关闭页面
        state_delete_device_management_class.close_web()

    # 被用户绑定不能删除

    # 视频开会 视频监控

