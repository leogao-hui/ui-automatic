#_author:leo gao
#encoding:utf-8

import allure
import pytest
import time


@allure.feature('删除组织架构的case')
@pytest.mark.usefixtures('add_organization_structure')
@pytest.mark.usefixtures('normal_login')
class TestDeleteOrganizationStructure:
    @allure.story('这是一个测试正常删除组织架构的case')
    def test_normal_delete_organization_structure(self, state_organization_structure_class):
        pass
        # '''
        # 用例描述：删除组织架构
        # :return:
        # '''
        # state_organization_structure_class.delete_organization_structure()
        # time.sleep(1)
        # assert '' in state_organization_structure_class.\
        #     assert_organization_structure_name()
        #
        # # 关闭页面
        # #state_organization_structure_class.close_web()

