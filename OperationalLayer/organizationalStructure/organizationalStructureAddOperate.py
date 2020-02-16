#_author:leo gao
#encoding:utf-8

import allure
from Base.base import Base
from ElementLayer.organizationalStructure.organizationalStructureElement import OrganizationalStructureElement


class OrganizationalStructureAddOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('点击组织架构')
    def click_organization_structure(self):
        self.click(OrganizationalStructureElement.organization_structure_button)

    @allure.step('点击总军区')
    def click_total_military_area_command(self):
        self.click(OrganizationalStructureElement.total_military_area_command)

    @allure.step('添加组织架构')
    def add_organization(self, serial_number, name):
        self.click(OrganizationalStructureElement.first_add_button)
        self.send_keys(OrganizationalStructureElement.add_organization_structure_serial_number_input, serial_number)
        self.send_keys(OrganizationalStructureElement.add_organization_structure_name_input, name)
        self.click(OrganizationalStructureElement.confirm_button)

    @allure.step('关闭页面')
    def close_web(self):
        self.close()

    @allure.step('验证新增组织结构名字')
    def assert_organization_structure_name(self):
        return self.get_txt_in_tag(OrganizationalStructureElement.assert_organization_name)





