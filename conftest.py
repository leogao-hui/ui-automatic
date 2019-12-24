#_author:leo gao
#encoding:utf-8

import pytest
from selenium import webdriver


driver_ = None


@pytest.fixture(scope='function')
def state_driver():
    # 定义全局参数driver
    global driver_
    driver_ = webdriver.Chrome()
    return driver_





