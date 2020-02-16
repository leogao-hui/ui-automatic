#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time
from Data.organizationStructure.modify_organization_structure_data import modify_organization_structure_data


@allure.feature('修改组织架构的case')
@pytest.mark.usefixtures('normal_login')
class TestAddUser:

    @allure.story('这是一个测试正常修改组织架构的case')
    def test_normal_modify_organization_structure(self, state_organization_structure_class):
        '''
        用例描述：修改编号，名字，正常修改组织架构
        :return:
        '''
        state_organization_structure_class.click_organization_structure()
        state_organization_structure_class.click_total_military_area_command()
        state_organization_structure_class.add_organization(
            modify_organization_structure_data.get('organization_structure_serial_number'),
            modify_organization_structure_data.get('organization_structure_name'))

        time.sleep(1)
        assert modify_organization_structure_data.get('organization_structure_name') in state_organization_structure_class.\
            assert_organization_structure_name()
        # 断言

        # 关闭页面
        state_organization_structure_class.close_web()