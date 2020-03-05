#_author:leo gao
#encoding:utf-8

# import exrex
import random
#
# print(exrex.getone(r'(13[0-9]|14[5|7]|15[4]|18[0-9]|17[5-8])(\d{8})'))
# #print(exrex.getone(r'(13[0-9]'))
#
#
# import random

# name = ''
# for i in range(0, 2):
#     name1 = chr(random.randint(0x4e00, 0x9fbf))
#     name += name1
# print(name)

# import random
#
# name = chr(random.randint(65, 90))
# print(name)

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
browser_url = r'C:\Users\keda\AppData\Local\Chromium\Application\chrome.exe'
chrome_options.binary_location = browser_url
web = webdriver.Chrome(options=chrome_options)

web.get('http://10.66.8.200:8088/#/login')
time.sleep(2)
web.find_element_by_xpath('//input[@class="username"]').send_keys('1111')
wb= web.find_element_by_xpath('//input[@class="username"]')
wb.send_keys(Keys.CONTROL + 'a')
wb.send_keys(Keys.BACKSPACE)

