#_author:leo gao
#encoding:utf-8


import allure
from Base.base import Base
from ElementLayer.organizationalStructure.organizationalStructureElement import OrganizationalStructureElement


class OrganizationalStructureDeleteOperate(Base):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    @allure.step('删除组织架构')
    def delete_organization_structure(self):
        self.click(OrganizationalStructureElement.organization_structure_button)