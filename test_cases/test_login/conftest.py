#_author:leo gao
#encoding:utf-8

import pytest
from operationalLayer.Login.login import LoginOperate
from operationalLayer.userManagement.userManagementAddOperate import UserManagementAddOperate
from Url.Login import login
from Url.userManagement import userManagement


@pytest.fixture()
def state_login_class(state_driver):
    login_operate = LoginOperate(state_driver, login.login_url)
    return login_operate


@pytest.fixture()
def state_add_user_management_class(state_driver):
    add_user_management_operate = UserManagementAddOperate(state_driver, userManagement.user_manager_url)
    return add_user_management_operate
