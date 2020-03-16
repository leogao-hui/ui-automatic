#_author:leo gao
#encoding:utf-8


import allure
from Base.base import Base
from elementLayer.organizationalStructure.organizationalStructureElement import OrganizationalStructureElement


class OrganizationalStructureDeleteOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('删除组织架构')
    def delete_organization_structure(self):
        self.use_js_click(OrganizationalStructureElement.first_organization_structure)
        self.use_js_click(OrganizationalStructureElement.first_organization_structure_delete_button)
        self.use_js_click(OrganizationalStructureElement.delete_confirm_button)
