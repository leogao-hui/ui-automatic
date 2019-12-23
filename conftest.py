#_author:leo gao
#encoding:utf-8

import pytest
from selenium import webdriver


driver_ = None


@pytest.fixture(scope='session')
def state_driver():
    # 定义全局参数driver
    global driver_
    # if driver_ is None:
    #     name = driver
    #     if name == "firefox":
    #         driver_ = webdriver.Firefox()
    #     elif name == "chrome":
    #         driver_ = webdriver.Chrome()
    #     else:
    #         print('您输入的driver不支持')
    #
    #     print("正在启动浏览器名称：%s" % name)
    driver_ = webdriver.Chrome()
    return driver_




