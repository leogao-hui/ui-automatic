#_author:leo gao
#encoding:utf-8

import pytest
from OperationalLayer.UserManagement.userManagementOperate import UserManagementOperate
from Url.userManagement import userManagement
from Data.Login import noraml_login_data, abnormal_login_data
from OperationalLayer.Login.login import LoginOperate
from Url.Login import login


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
def state_user_management_class(state_driver):
    user_management_operate = UserManagementOperate(state_driver, userManagement.user_manager_url)
    return user_management_operate

