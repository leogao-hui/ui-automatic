#_author:leo gao
#encoding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://10.66.8.200:8088/')
driver.find_element_by_class_name('username').send_keys('admin12')
driver.find_element_by_class_name('password').send_keys('admin123')
driver.find_element_by_xpath('//*[@class="idcode"]/input').send_keys('1111')
driver.find_element_by_class_name('login-confirm').click()
time.sleep(1)
aa = driver.find_element_by_class_name('modalText').get_attribute("innerHTML")


print(aa)