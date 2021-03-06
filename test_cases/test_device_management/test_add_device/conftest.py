#_author:leo gao
#encoding:utf-8

import pytest
from operationalLayer.Login.login import LoginOperate
from operationalLayer.deviceManagement.deviceManagementAddOperate import DeviceManagementAddOperate
from Url.deviceManagement import deviceManagement
from Url.Login import login
from Data.Login import noraml_login_data
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
def state_add_device_management_class(state_driver):
    add_device_management_operate = DeviceManagementAddOperate(state_driver, deviceManagement.device_manager_url)
    return add_device_management_operate


# @pytest.fixture()
# def add_device_fixture(state_add_device_management_class):
#     state_add_device_management_class.click_device_management()
#     state_add_device_management_class.input_device_name_ip(
#         normal_add_device_data.normal_add_device_data.get('device_name'),
#         normal_add_device_data.normal_add_device_data.get('device_ip'))
#     state_add_device_management_class.choose_device_type()
#     state_add_device_management_class.choose_organization_manufacturer(normal_add_device_data.
#                                                                        normal_add_device_data.get('manufacturer'))


@pytest.fixture(scope='function', autouse=True)
def database_base_configuration():
    delete_database_data_test_ci()
    add_database_data_test_ci()