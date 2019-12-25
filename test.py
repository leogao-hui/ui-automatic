#_author:leo gao
#encoding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://10.66.8.200:8088/')
driver.find_element_by_class_name('username').send_keys('admin')
driver.find_element_by_class_name('password').send_keys('admin123')
driver.find_element_by_xpath('//*[@class="idcode"]/input').send_keys('1111')
driver.find_element_by_class_name('login-confirm').click()
time.sleep(2)
driver.find_element_by_xpath("//*[text()='用户管理']").click()
driver.find_element_by_xpath('//*[text()="添加"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[2]/div/div/div/div[2]/ul/li[1]/input').send_keys('aa')

driver.find_element_by_xpath('//*[@class="adduser-content-main"]/ul/li[5]/input').click()
driver.find_element_by_xpath('//*[@class="orgstructure-scroll-treebox"]/div/li/div/span/span/span').click()