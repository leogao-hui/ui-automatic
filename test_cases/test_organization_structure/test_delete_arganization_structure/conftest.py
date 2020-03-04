#_author:leo gao
#encoding:utf-8


import pytest
from operationalLayer.Login.login import LoginOperate
from operationalLayer.organizationalStructure.organizationalStructureAddOperate import OrganizationalStructureAddOperate
from Url.Login import login
from Data.Login import noraml_login_data
from Data.organizationStructure.add_organization_structure import add_organization_structure_data, \
    name_repeat_organization_structure


@pytest.fixture()
def state_login_class(state_driver):
    login_operate = LoginOperate(state_driver, login.login_url)
    return login_operate


@pytest.fixture()
def normal_login(state_login_class):
    '''
    用例描述：输入正确管理员账号，正确密码，验证码（随便）正常登录
    :return:
    '''

    state_login_class.get_login_url()
    state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                    noraml_login_data.verification_code)
    state_login_class.confirm_login_button()


@pytest.fixture()
def state_organization_structure_class(state_driver):
    organization_structure_operate = OrganizationalStructureAddOperate(state_driver, login.login_url)
    return organization_structure_operate


@pytest.fixture()
def add_organization_structure(state_organization_structure_class):
    state_organization_structure_class.click_organization_structure()
    state_organization_structure_class.click_total_military_area_command()
    state_organization_structure_class.add_organization(
        add_organization_structure_data.add_organization_structure_data.get('organization_structure_serial_number'),
        add_organization_structure_data.add_organization_structure_data.get('organization_structure_name'))

