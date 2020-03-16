#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from elementLayer.organizationalStructure.organizationalStructureElement import OrganizationalStructureElement


class OrganizationalStructureModifyOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('修改组织架构')
    def modify_organization_structure(self, modify_name):
        self.use_js_click(OrganizationalStructureElement.first_organization_structure)
        self.use_js_click(OrganizationalStructureElement.first_organization_structure_modify_button)
        self.clear(OrganizationalStructureElement.modify_organization_structure_name_input)
        self.send_keys(OrganizationalStructureElement.modify_organization_structure_name_input, modify_name)
        self.use_js_click(OrganizationalStructureElement.modify_name_confirm_button)

    @allure.step('验证修改组织结构名字')
    def assert_organization_structure_name(self):
        return self.get_txt_in_tag(OrganizationalStructureElement.assert_organization_name)

    @allure.step('关闭页面')
    def close_web(self):
        self.close()





