#_author:leo gao
#encoding:utf-8

import pytest
from OperationalLayer.Login.login import LoginOperate
from OperationalLayer.deviceManagement.deviceManagementAddOperate import DeviceManagementAddOperate
from OperationalLayer.deviceManagement.deviceManagementModifyOperate import DeviceManagementModifyOperate
from OperationalLayer.systemManagement.systemManagementAddOperate import SystemManagementAddOperate
from Url.Login import login
from Url.deviceManagement import deviceManagement
from Url.systemManagement import systemManagement
from Data.Login import noraml_login_data
from Data.deviceManagement.add_device import normal_add_device_data
from Data.SystemManagement import systemManagementData


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


@pytest.fixture()
def add_device_fixture(state_add_device_management_class):
    state_add_device_management_class.click_device_management()
    state_add_device_management_class.input_device_name_ip(
        normal_add_device_data.normal_add_device_data.get('device_name'),
        normal_add_device_data.normal_add_device_data.get('device_ip'))
    state_add_device_management_class.choose_device_type()
    state_add_device_management_class.choose_organization_manufacturer(normal_add_device_data.
                                                                       normal_add_device_data.get('manufacturer'))


@pytest.fixture()
def state_modify_device_management_class(state_driver):
    modify_device_management_operate = DeviceManagementModifyOperate(state_driver, deviceManagement.device_manager_url)
    return modify_device_management_operate


# @pytest.fixture()
# def state_add_system_device_management_class(state_driver):
#     add_system_device_operate = SystemManagementAddOperate(state_driver, systemManagement.system_manager_url)
#     return add_system_device_operate
#
#
# @pytest.fixture()
# def add_system_device(state_add_system_device_management_class):
#     state_add_system_device_management_class.add_device_server(systemManagementData.add_device_server.get('name'),
#                                                                systemManagementData.add_device_server.get('ip'),
#                                                                systemManagementData.add_device_server.get('port'))
