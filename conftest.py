#_author:leo gao
#encoding:utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_ = None


@pytest.fixture(scope='function')
def state_driver():
    chrome_options = Options()
    browser_url = r'C:\Users\keda\AppData\Local\Chromium\Application\chrome.exe'
    chrome_options.binary_location = browser_url
    # chrome_options.add_argument('--headless')  # 无界面
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
    chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
    chrome_options.add_argument('log-level=3') # 设置日志等级
    # 定义全局参数driver
    global driver_
    driver_ = webdriver.Chrome(options=chrome_options)
    return driver_





