#_author:leo gao
#encoding:utf-8

import pytest
import time
from OperationalLayer.userManagement.userManagementAddOperate import UserManagementAddOperate
from OperationalLayer.userManagement.userManagementModifyOperate import UserManagementModifyOperate
from OperationalLayer.Login.login import LoginOperate
from Url.userManagement import userManagement
from Url.Login import login
from Data.Login import noraml_login_data
from Data.userManagement.modify_user import modify_user_name_data


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
def state_add_user_management_class(state_driver):
    add_user_management_operate = UserManagementAddOperate(state_driver, userManagement.user_manager_url)
    return add_user_management_operate


@pytest.fixture()
def add_user(state_add_user_management_class):
    state_add_user_management_class.click_user_management()
    state_add_user_management_class.add_user(modify_user_name_data.modify_user_name_data['serial_num'],
                                             modify_user_name_data.modify_user_name_data['name'],
                                             modify_user_name_data.modify_user_name_data['account'])
    state_add_user_management_class.choose_organization()
    time.sleep(1)
    state_add_user_management_class.confirm()


@pytest.fixture()
def state_modify_user_management_class(state_driver):
    modify_user_management_operate = UserManagementModifyOperate(state_driver, userManagement.user_manager_url)
    return modify_user_management_operate
