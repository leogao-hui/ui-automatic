#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class OrganizationalStructureElement:

    # 组织架构按钮
    organization_structure_button = (By.XPATH, '//*[text()="组织架构"]')

    # 总军区
    total_military_area_command = (By.XPATH, '//*[@class="organization-tree"]/div/li/div/span/span')

    # 第一个添加
    first_add_button = (By.XPATH, '//*[@class="organization-tree"]/div/li/div/span/span[2]/span')

    # 第一个编辑
    first_edit_button = (By.XPATH, '//*[@class="organization-tree"]/div/li/div/span/span[2]/span[2]')

    # 添加组织架构编号
    add_organization_structure_serial_number_input = (By.XPATH,
                                                      '//*[@class="organization-tree"]/div/div/div/div[2]/ul/li/input')

    # 添加组织架构名称
    add_organization_structure_name_input = (By.XPATH,
                                             '//*[@class="organization-tree"]/div/div/div/div[2]/ul/li[2]/input')

