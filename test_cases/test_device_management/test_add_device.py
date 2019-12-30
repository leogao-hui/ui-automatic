# _author:leo gao
# encoding:utf-8

import allure
import pytest
import time
from Data.deviceManagement.add_device import normal_add_device_data


@pytest.mark.usefixtures('normal_login')
@allure.feature('设备管理')
class TestAddDevice:

    @allure.story('这是一个测试正常新增设备的case')
    def test_normal_add_device(self, state_add_device_management_class):
        '''
        用例描述：输入设备编号，设备ip，生产厂家，选择设备类型，组织机构，正常新增设备
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            normal_add_device_data.normal_add_device_data.get('device_name'),
            normal_add_device_data.normal_add_device_data.get('device_ip'))
        state_add_device_management_class.choose_device_type()

        state_add_device_management_class.choose_organization_manufacturer(normal_add_device_data.
                                                                           normal_add_device_data.get('manufacturer'))

        assert '1' == state_add_device_management_class.assert_serial_number()
        assert normal_add_device_data.normal_add_device_data.get('device_name') == state_add_device_management_class. \
            assert_device_name()
        assert normal_add_device_data.normal_add_device_data.get('device_ip') == state_add_device_management_class. \
            assert_device_ip()
        assert normal_add_device_data.normal_add_device_data.get('manufacturer') == state_add_device_management_class. \
            assert_manufacturer()
        assert '编码器' == state_add_device_management_class.assert_device_type()
        # 关闭页面
        state_add_device_management_class.close_web()

    # @allure.story('这是一个测试设备名称必填项的case')
    # def test_device_name_mandatory(self, state_add_device_management_class, state_driver):
    #     '''
    #     用例描述：设备名称必填
    #     :return:
    #     '''
    #     state_add_device_management_class.click_device_management()
    #     state_add_device_management_class.input_device_name_ip('',
    #                                                            normal_add_device_data.normal_add_device_data.get(
    #                                                                'device_ip'))
    #     device_type_element = state_driver. \
    #         find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input')
    #     encode_element = state_driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span')
    #     state_add_device_management_class.choose_device_type(device_type_element, encode_element)
    #     state_add_device_management_class.choose_organization_manufacturer(normal_add_device_data.
    #                                                                        normal_add_device_data.get('manufacturer'))
    #     assert '请输入正确的设备信息' == state_add_device_management_class.assert_error_information()
    #
    # @allure.story('这是一个测试设备ip必填项的case')
    # def test_device_ip_mandatory(self, state_add_device_management_class, state_driver):
    #     '''
    #     用例描述：设备ip必填
    #     :param state_add_device_management_class:
    #     :param state_driver:
    #     :return:
    #     '''
    #     state_add_device_management_class.click_device_management()
    #     state_add_device_management_class.input_device_name_ip(normal_add_device_data.normal_add_device_data.get(
    #         'device_name'), '')
    #     device_type_element = state_driver. \
    #         find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input')
    #     encode_element = state_driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span')
    #     state_add_device_management_class.choose_device_type(device_type_element, encode_element)
    #     state_add_device_management_class.choose_organization_manufacturer(normal_add_device_data.
    #                                                                        normal_add_device_data.get('manufacturer'))
    #     assert '请输入正确的设备信息' == state_add_device_management_class.assert_error_information()
    #
    # @allure.story('这是一个测试设备生产厂家必填的case')
    # def test_manufacturer_mandatory(self, state_add_device_management_class, state_driver):
    #     '''
    #     用例描述：设备生产厂家必填
    #     :param state_add_device_management_class:
    #     :param state_driver:
    #     :return:
    #     '''
    #     state_add_device_management_class.click_device_management()
    #     state_add_device_management_class.input_device_name_ip(normal_add_device_data.normal_add_device_data.get(
    #         'device_name'), normal_add_device_data.normal_add_device_data.get('device_ip'))
    #     device_type_element = state_driver. \
    #         find_element_by_xpath('//*[@class="manage-main"]/div[2]/div/div/div/div[2]/ul/li[3]/div/div/input')
    #     encode_element = state_driver.find_element_by_xpath('//*[@class="el-scrollbar"]/div/ul/li/span')
    #     state_add_device_management_class.choose_device_type(device_type_element, encode_element)
    #     state_add_device_management_class.choose_organization_manufacturer('')
    #     assert '请输入正确的设备信息' == state_add_device_management_class.assert_error_information()
    #
