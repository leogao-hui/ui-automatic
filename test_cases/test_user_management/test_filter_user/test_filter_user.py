#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time
from Data.userManagement.add_user import filter_add_user_data


@allure.feature('成员管理,过滤人员')
@pytest.mark.usefixtures('normal_login')
class TestFilterUser:
    pass

    # @allure.story('这是一条过滤编号的case')
    # def test_filter_serial_number(self, state_add_user_management_class):
    #     '''
    #     用例描述：新增4个人员
    #     :return:
    #     '''
    #     for key in filter_add_user_data.filter_add_user_data:
    #         state_add_user_management_class.click_user_management()
    #         state_add_user_management_class.add_user(
    #             filter_add_user_data.filter_add_user_data[key]['serial_num'],
    #             filter_add_user_data.filter_add_user_data[key]['name'],
    #             filter_add_user_data.filter_add_user_data[key]['account'])
    #         state_add_user_management_class.choose_organization()
    #         time.sleep(1)
    #         state_add_user_management_class.confirm()
    #         # 断言