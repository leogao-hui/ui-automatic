#_author:leo gao
#encoding:utf-8

import pytest
from Utils.operateDatabaseData import delete_database_data_test_ci, add_database_data_test_ci
from conftest import state_driver
from OperationalLayer.Login.login import LoginOperate
from Url.Login import login


@pytest.fixture(scope='class', autouse=True)
def database_base_configuration():
    delete_database_data_test_ci()
    add_database_data_test_ci()


@pytest.fixture(scope='class', autouse=True)
def state_login_class():
    login_operate = LoginOperate(state_driver, login.login_url)
    return login_operate
