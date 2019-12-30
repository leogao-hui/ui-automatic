#_author:leo gao
#encoding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://10.66.8.200:8088/#/manage')
driver.find_element_by_class_name('username').send_keys('admin')
driver.find_element_by_class_name('password').send_keys('admin123')
driver.find_element_by_xpath('//*[@class="idcode"]/input').send_keys('1111')
driver.find_element_by_class_name('login-confirm').click()
time.sleep(2)
driver.find_element_by_xpath("//*[text()='设备管理']").click()

driver.find_element_by_xpath('//*[text()="添加"]').click()
driver.find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li/input').send_keys('11')

# 第一种直接点击
# driver.find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input').click()
# driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span').click()


# 第二种js点击
driver.find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input').click()
button = driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span')
driver.execute_script("(arguments[0]).click();", button)


# js = 'document.getElementsByClassName("el-select-dropdown__item deviceItem playeropt")[0].click();'

# time.sleep(3)
# WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span')))
#driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span').click()
#button = driver.find_element_by_xpath('//*[text()="编码器"]')
#button = driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span')
#driver.execute_script("(arguments[0]).click();",button)



#driver.close()