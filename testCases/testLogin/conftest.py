#_author:leo gao
#encoding:utf-8

import pytest
from OperationalLayer.Login.login import LoginOperate
from Url.Login import login


@pytest.fixture()
def state_login_class(state_driver):
    login_operate = LoginOperate(state_driver, login.login_url)
    return login_operate
