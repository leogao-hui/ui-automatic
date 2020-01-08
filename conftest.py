#_author:leo gao
#encoding:utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_ = None


@pytest.fixture(scope='function')
def state_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 定义全局参数driver
    global driver_
    driver_ = webdriver.Chrome(options=chrome_options)
    return driver_





