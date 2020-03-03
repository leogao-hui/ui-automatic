#_author:leo gao
#encoding:utf-8


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base:

    '''基于原生的selenium做二次封装'''

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.timeout = 5
        self.t = 0.5

    # 定位元素
    def find_element(self, locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def find_elements(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
                return eles
            except:
                return []

    # 输入内容
    def send_keys(self, locator, text=''):
        ele = self.find_element(locator)
        ele.send_keys(text)

    # 点击
    def click(self, locator):
        ele = self.find_element(locator)
        ele.click()

    # 获取当前网页url
    def receive_current_url(self):
        return self.driver.current_url

    # 到达网页
    def get_url(self):
        return self.driver.get(self.url)

    # 清空数据
    def clear(self, locator):
        ele = self.find_element(locator)
        ele.clear()

    # 关闭页面
    def close(self):
        self.driver.close()

    # 关闭页面
    def quit(self):
        self.driver.quit()

    # 获取页面handle
    def get_handle(self):
        handle = self.driver.current_window_handle
        return handle

    # action
    def continuous_operate(self, locator_one, locator_two):
        ActionChains(self.driver).click(locator_one).click(locator_two).perform()

    # 获取标签内容
    def get_txt_in_tag(self, locator):
        return self.find_element(locator).get_attribute("textContent")

    # 使用js点击
    def use_js_click(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("(arguments[0]).click()", target)

    def is_selected(self, locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.find_element(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def is_title(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def switch_window(self, window):
        return self.driver.switch_to_window(window)


