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

    # 确认按钮
    confirm_button = (By.XPATH, '//*[@class="organization-tree"]/div/div/div/div[3]/button[1]')

    # 验证组织架构名称
    assert_organization_name = (By.XPATH, '//*[@class="organization-tree"]/div/li/ul/div/li/div/span/span[1]')

    # 第一个组织架构
    first_organization_structure = (By.XPATH, '//*[@class="organization-tree"]/div/li/ul/div/li/div/span/span[1]')

    # 第一个组织架构修改按钮
    first_organization_structure_modify_button = (By.XPATH, '//*[@class="organization-tree"]/div/li/ul/div/li/div/span/span[2]/span[2]')

    # 第一个组织架构删除按钮
    first_organization_structure_delete_button = (By.XPATH, '//*[@class="organization-tree"]/div/li/ul/div/li/div/span/span[2]/span[3]')

    # 确认按钮
    delete_confirm_button = (By.XPATH, '//*[@class="frame"]/div[3]/button[1]')