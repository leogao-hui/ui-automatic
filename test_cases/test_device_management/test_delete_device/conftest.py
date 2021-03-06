#_author:leo gao
#encoding:utf-8

import pytest
from operationalLayer.Login.login import LoginOperate
from operationalLayer.deviceManagement.deviceManagementAddOperate import DeviceManagementAddOperate
from operationalLayer.deviceManagement.deviceManagementDeleteOperate import DeviceManagementDeleteOperate
from operationalLayer.userManagement.userManagementAddOperate import UserManagementAddOperate
from Url.userManagement import userManagement
from Url.deviceManagement import deviceManagement
from Url.Login import login
from Data.Login import noraml_login_data
from Data.deviceManagement.add_device import normal_add_device_data


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
def state_add_user_management_class(state_driver):
    add_user_management_operate = UserManagementAddOperate(state_driver, userManagement.user_manager_url)
    return add_user_management_operate


@pytest.fixture()
def state_delete_device_management_class(state_driver):
    delete_device_management_operate = DeviceManagementDeleteOperate(state_driver, deviceManagement.device_manager_url)
    return delete_device_management_operate
