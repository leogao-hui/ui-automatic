#_author:leo gao
#encoding:utf-8


import pytest
from OperationalLayer.Login.login import LoginOperate
from OperationalLayer.organizationalStructure.organizationalStructureAddOperate import OrganizationalStructureAddOperate
from OperationalLayer.organizationalStructure.organizationalStructureModifyOperate import OrganizationalStructureModifyOperate
from Url.Login import login
from Data.Login import noraml_login_data
from Data.organizationStructure.modify_organization_structure import modify_organization_structure_data
from Utils.operateDatabaseData import delete_database_data_test_ci, add_database_data_test_ci


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
def state_add_organization_structure_class(state_driver):
    organization_structure_add_operate = OrganizationalStructureAddOperate(state_driver, login.login_url)
    return organization_structure_add_operate


@pytest.fixture()
def add_organization_structure(state_add_organization_structure_class):
    state_add_organization_structure_class.click_organization_structure()
    state_add_organization_structure_class.click_total_military_area_command()
    state_add_organization_structure_class.add_organization(
        modify_organization_structure_data.add_organization_structure_data.get('organization_structure_serial_number'),
        modify_organization_structure_data.add_organization_structure_data.get('organization_structure_name'))


@pytest.fixture()
def state_modify_organization_structure_class(state_driver):
    organization_structure_modify_operate = OrganizationalStructureModifyOperate(state_driver, login.login_url)
    return organization_structure_modify_operate


@pytest.fixture(scope='function', autouse=True)
def database_base_configuration():
    delete_database_data_test_ci()
    add_database_data_test_ci()
