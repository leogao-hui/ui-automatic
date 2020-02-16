#_author:leo gao
#encoding:utf-8


import allure
import pytest
import time
from Data.organizationStructure.organizationStructureData import add_organization_structure_data


@allure.feature('新增组织架构的case')
@pytest.mark.usefixtures('normal_login')
class TestAddUser:

    @allure.story('这是一个测试正常新增组织架构的case')
    def test_normal_add_user(self, state_organization_structure_class):
        '''
        用例描述：输入编号，名字，正常新增组织架构
        :return:
        '''
        state_organization_structure_class.click_organization_structure()
        state_organization_structure_class.click_total_military_area_command()
        state_organization_structure_class.add_organization(
            add_organization_structure_data.get('organization_structure_serial_number'),
            add_organization_structure_data.get('organization_structure_name'))

        time.sleep(1)
        assert add_organization_structure_data.get('organization_structure_name') in state_organization_structure_class.\
            assert_organization_structure_name()

        # 关闭页面
        state_organization_structure_class.close_web()

    @allure.story('这是一个测试新增多个组织架构的case')
    def test_normal_add_user(self, state_organization_structure_class):
        '''
        用例描述：输入编号，名字，正常新增组织架构
        :return:
        '''
        state_organization_structure_class.click_organization_structure()
        state_organization_structure_class.click_total_military_area_command()
        state_organization_structure_class.add_organization(
            add_organization_structure_data.get('organization_structure_serial_number'),
            add_organization_structure_data.get('organization_structure_name'))

        # 加

        time.sleep(1)
        assert add_organization_structure_data.get('organization_structure_name') in state_organization_structure_class. \
            assert_organization_structure_name()

        # 关闭页面
        state_organization_structure_class.close_web()

    @allure.story('这是一个测试删除组织架构的case')
    def test_normal_add_user(self, state_organization_structure_class):
        '''
        用例描述：删除单个组织架构
        :return:
        '''
        state_organization_structure_class.click_organization_structure()
        state_organization_structure_class.click_total_military_area_command()
        state_organization_structure_class.add_organization(
            add_organization_structure_data.get('organization_structure_serial_number'),
            add_organization_structure_data.get('organization_structure_name'))

        # 删除

        time.sleep(1)
        assert add_organization_structure_data.get('organization_structure_name') in state_organization_structure_class. \
            assert_organization_structure_name()

        # 关闭页面
        state_organization_structure_class.close_web()

