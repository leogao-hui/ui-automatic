#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time
from Data.organizationStructure.modify_organization_structure import modify_organization_structure_data


@allure.feature('修改组织架构的case')
@pytest.mark.usefixtures('add_organization_structure')
@pytest.mark.usefixtures('normal_login')
class TestModifyOrganizationStructure:
    pass

    # @allure.story('这是一个测试正常修改组织架构的case')
    # def test_normal_modify_organization_structure(self, state_modify_organization_structure_class):
    #     '''
    #     用例描述：修改编号，名字，正常修改组织架构
    #     :return:
    #     '''
    #     time.sleep(1)
    #     state_modify_organization_structure_class.modify_organization_structure(modify_organization_structure_data)
    #
    #     assert modify_organization_structure_data.modify_organization_structure_data.get(
    #         'organization_structure_name') in state_modify_organization_structure_class.\
    #         assert_organization_structure_name()
    #
    #     # 关闭页面
    #     state_modify_organization_structure_class.close_web()
