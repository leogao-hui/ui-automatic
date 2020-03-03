# _author:leo gao
# encoding:utf-8

import allure
import pytest
import time
from Data.deviceManagement.add_device import normal_add_device_data, device_name_empty_add_device_data, \
    device_ip_empty_add_device_data, device_manufacturer_empty_add_device_data, name_check_again_add_device_data, \
    ip_check_again_add_device_data, device_filter_add_device_data, name_support_chinese_english_digital_add_device_data, \
    name_not_support_special_characters_add_device_data, name_support_sixteen_character_add_device_data, \
    name_support_fifteen_character_add_device_data, name_not_support_seventeen_character_add_device_data, \
    manufacturer_support_chinese_english_digital_add_device_data, \
    manufacturer_not_support_special_characters_add_device_data, \
    manufacturer_support_sixteen_character_add_device_data, manufacturer_support_fifteen_character_add_device_data, \
    manufacturer_not_support_seventeen_character_add_device_data


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

        assert normal_add_device_data.normal_add_device_data.get('device_name') == state_add_device_management_class. \
            assert_device_name()
        assert normal_add_device_data.normal_add_device_data.get('device_ip') == state_add_device_management_class. \
            assert_device_ip()
        assert normal_add_device_data.normal_add_device_data.get('manufacturer') == state_add_device_management_class. \
            assert_manufacturer()
        assert '编码器' == state_add_device_management_class.assert_device_type()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一个测试设备名称必填项的case')
    def test_device_name_mandatory(self, state_add_device_management_class):
        '''
        用例描述：设备名称必填
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(device_name_empty_add_device_data.
                                                               device_name_empty_data.get('device_name'),
                                                               device_name_empty_add_device_data.
                                                               device_name_empty_data.get('device_ip'))
        state_add_device_management_class.choose_device_type()

        state_add_device_management_class.choose_organization_manufacturer(device_name_empty_add_device_data.
                                                                           device_name_empty_data.get('manufacturer'))
        time.sleep(2)
        assert '请输入正确的设备信息' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一个测试设备ip必填项的case')
    def test_device_ip_mandatory(self, state_add_device_management_class):
        '''
        用例描述：设备ip必填
        :param state_add_device_management_class:
        :param state_driver:
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(device_ip_empty_add_device_data.
                                                               device_ip_empty_data.get('device_name'),
                                                               device_ip_empty_add_device_data.
                                                               device_ip_empty_data.get('device_ip'))
        state_add_device_management_class.choose_device_type()

        state_add_device_management_class.choose_organization_manufacturer(device_name_empty_add_device_data.
                                                                           device_name_empty_data.get('manufacturer'))
        time.sleep(2)
        assert '请输入正确的设备信息' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一个测试设备生产厂家必填的case')
    def test_manufacturer_mandatory(self, state_add_device_management_class):
        '''
        用例描述：设备生产厂家必填
        :param state_add_device_management_class:
        :param state_driver:
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(device_manufacturer_empty_add_device_data.
                                                               device_manufacturer_empty_data.get('device_name'),
                                                               device_manufacturer_empty_add_device_data.
                                                               device_manufacturer_empty_data.get('device_ip'))
        state_add_device_management_class.choose_device_type()

        state_add_device_management_class.choose_organization_manufacturer(device_manufacturer_empty_add_device_data.
                                                                           device_manufacturer_empty_data.
                                                                           get('manufacturer'))
        time.sleep(2)
        assert '请输入正确的设备信息' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一个测试设备名称验重的case')
    def test_name_check_again(self, state_add_device_management_class):
        '''
        用例描述：名称验重
        :param state_add_device_management_class:
        :param state_driver:
        :return:
        '''
        for key in name_check_again_add_device_data.name_check_again_add_device_data:
            state_add_device_management_class.click_device_management()
            state_add_device_management_class.input_device_name_ip(name_check_again_add_device_data.
                name_check_again_add_device_data[key].get(
                'device_name'),
                name_check_again_add_device_data.
                name_check_again_add_device_data[key].get(
                    'device_ip'))
            state_add_device_management_class.choose_device_type()
            state_add_device_management_class.choose_organization_manufacturer(name_check_again_add_device_data.
                                                                               name_check_again_add_device_data[
                                                                                   key].get('manufacturer'))
            time.sleep(2)
        assert 'IP已经绑定在其他设备' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一个测试设备ip验重的case')
    def test_ip_check_again(self, state_add_device_management_class):
        '''
        用例描述：ip验重
        :param state_add_device_management_class:
        :param state_driver:
        :return:
        '''
        for key in ip_check_again_add_device_data.ip_check_again_add_device_data:
            state_add_device_management_class.click_device_management()
            state_add_device_management_class.input_device_name_ip(
                ip_check_again_add_device_data.ip_check_again_add_device_data[key].get('device_name'),
                ip_check_again_add_device_data.ip_check_again_add_device_data[key].get('device_ip'))
            state_add_device_management_class.choose_device_type()
            state_add_device_management_class.choose_organization_manufacturer(
                ip_check_again_add_device_data.ip_check_again_add_device_data[key].get('manufacturer'))
            time.sleep(2)
        assert 'IP已经绑定在其他设备' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    # @allure.story('这是一个过滤设备的case')
    # def test_device_filter_again(self, state_add_device_management_class):
    #     '''
    #     用例描述：过滤设备
    #     :param state_add_device_management_class:
    #     :param state_driver:
    #     :return:
    #     '''
    #     for key in device_filter_add_device_data.device_filter_data:
    #         state_add_device_management_class.click_device_management()
    #         state_add_device_management_class.input_device_name_ip(key.get('name'),
    #                                                                key.get('device_ip'))
    #         state_add_device_management_class.choose_device_type()
    #         state_add_device_management_class.choose_organization_manufacturer(key.get('manufacturer'))
    #         time.sleep(2)
    #     # 过滤
    #
    #     # 关闭页面
    #     state_add_device_management_class.close_web()

    @allure.story('这是一条测试设备名称支持中文，英文，数字的case')
    def test_name_support_chinese_english_digital(self, state_add_device_management_class):
        '''
        用例描述：设备名称支持中文，英文，数字，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(name_support_chinese_english_digital_add_device_data.
                                                               name_support_chinese_english_digital_add_device_data[
                                                                   'device_name'],
                                                               name_support_chinese_english_digital_add_device_data.
                                                               name_support_chinese_english_digital_add_device_data[
                                                                   'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            name_support_chinese_english_digital_add_device_data.
                name_support_chinese_english_digital_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert name_support_chinese_english_digital_add_device_data.name_support_chinese_english_digital_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()
        assert name_support_chinese_english_digital_add_device_data.name_support_chinese_english_digital_add_device_data.get(
            'device_ip') == state_add_device_management_class. \
                   assert_device_ip()
        assert name_support_chinese_english_digital_add_device_data.name_support_chinese_english_digital_add_device_data.get(
            'manufacturer') == state_add_device_management_class. \
                   assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条测试设备名称不支持特殊字符的case')
    def test_name_not_support_special_characters(self, state_add_device_management_class):
        '''
        用例描述：设备名称不支持特殊字符，报错
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(name_not_support_special_characters_add_device_data.
                                                               name_not_support_special_characters_add_device_data[
                                                                   'device_name'],
                                                               name_not_support_special_characters_add_device_data.
                                                               name_not_support_special_characters_add_device_data[
                                                                   'device_ip'])
        time.sleep(1)
        assert '成功' in state_add_device_management_class.validate_bounced_error_information()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条生产工厂名称支持中文，英文，数字的case')
    def test_manufacturer_support_chinese_english_digital(self, state_add_device_management_class):
        '''
        用例描述：生产工厂支持中文，英文，数字，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            manufacturer_support_chinese_english_digital_add_device_data.
                manufacturer_support_chinese_english_digital_add_device_data[
                'device_name'],
            manufacturer_support_chinese_english_digital_add_device_data.
                manufacturer_support_chinese_english_digital_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            manufacturer_support_chinese_english_digital_add_device_data.
                manufacturer_support_chinese_english_digital_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert manufacturer_support_chinese_english_digital_add_device_data.manufacturer_support_chinese_english_digital_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()
        assert manufacturer_support_chinese_english_digital_add_device_data.manufacturer_support_chinese_english_digital_add_device_data.get(
            'device_ip') == state_add_device_management_class. \
                   assert_device_ip()
        assert manufacturer_support_chinese_english_digital_add_device_data.manufacturer_support_chinese_english_digital_add_device_data.get(
            'manufacturer') == state_add_device_management_class. \
                   assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条生产工厂名称不支持特殊字符的case')
    def test_manufacturer_not_support_special_characters(self, state_add_device_management_class):
        '''
        用例描述：不支持特殊字符，报错
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            manufacturer_not_support_special_characters_add_device_data.
                manufacturer_not_support_special_characters_add_device_data[
                'device_name'],
            manufacturer_not_support_special_characters_add_device_data.
                manufacturer_not_support_special_characters_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer_extra(
            manufacturer_not_support_special_characters_add_device_data.
                manufacturer_not_support_special_characters_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert '生产厂商仅支持中文,英文与数字!' in state_add_device_management_class.validate_bounced_error_information()

        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条测试设备名称支持16位的case')
    def test_name_support_sixteen_character(self, state_add_device_management_class):
        '''
        用例描述：设备名称16位，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            name_support_sixteen_character_add_device_data.
                name_support_sixteen_character_add_device_data[
                'device_name'],
            name_support_sixteen_character_add_device_data.
                name_support_sixteen_character_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            name_support_sixteen_character_add_device_data.
                name_support_sixteen_character_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert name_support_sixteen_character_add_device_data.name_support_sixteen_character_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()

        assert name_support_sixteen_character_add_device_data.name_support_sixteen_character_add_device_data.get(
            'device_ip') == state_add_device_management_class.assert_device_ip()

        assert name_support_sixteen_character_add_device_data.name_support_sixteen_character_add_device_data.get(
            'manufacturer') == state_add_device_management_class.assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条测试设备名称不支持17位的case')
    def test_name_not_support_seventeen_character(self, state_add_device_management_class):
        '''
        用例描述：设备名称17位，报错
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            name_not_support_seventeen_character_add_device_data.
                name_not_support_seventeen_character_add_device_data[
                'device_name'],
            name_not_support_seventeen_character_add_device_data.
                name_not_support_seventeen_character_add_device_data[
                'device_ip'])

    # 断言

    @allure.story('这是一条测试设备名称支持15位的case')
    def test_name_support_fifteen_character(self, state_add_device_management_class):
        '''
        用例描述：设备名称15位，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            name_support_fifteen_character_add_device_data.
                name_support_fifteen_character_add_device_data[
                'device_name'],
            name_support_fifteen_character_add_device_data.
                name_support_fifteen_character_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            name_support_fifteen_character_add_device_data.
                name_support_fifteen_character_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert name_support_fifteen_character_add_device_data.name_support_fifteen_character_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()

        assert name_support_fifteen_character_add_device_data.name_support_fifteen_character_add_device_data.get(
            'device_ip') == state_add_device_management_class.assert_device_ip()

        assert name_support_fifteen_character_add_device_data.name_support_fifteen_character_add_device_data.get(
            'manufacturer') == state_add_device_management_class.assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()

    @allure.story('这是一条测试生产厂家支持16位的case')
    def test_manufacturer_support_sixteen_character(self, state_add_device_management_class):
        '''
        用例描述：生产厂家16位，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            manufacturer_support_sixteen_character_add_device_data.
                manufacturer_support_sixteen_character_add_device_data[
                'device_name'],
            manufacturer_support_sixteen_character_add_device_data.
                manufacturer_support_sixteen_character_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            manufacturer_support_sixteen_character_add_device_data.
                manufacturer_support_sixteen_character_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert manufacturer_support_sixteen_character_add_device_data.manufacturer_support_sixteen_character_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()

        assert manufacturer_support_sixteen_character_add_device_data.manufacturer_support_sixteen_character_add_device_data.get(
            'device_ip') == state_add_device_management_class.assert_device_ip()

        assert manufacturer_support_sixteen_character_add_device_data.manufacturer_support_sixteen_character_add_device_data.get(
            'manufacturer') == state_add_device_management_class.assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()


    @allure.story('这是一条测试生产厂家支持15位的case')
    def test_manufacturer_support_fifteen_character(self, state_add_device_management_class):
        '''
        用例描述：生产厂家15位，正常新增
        :return:
        '''
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(
            manufacturer_support_fifteen_character_add_device_data.
                manufacturer_support_fifteen_character_add_device_data[
                'device_name'],
            manufacturer_support_fifteen_character_add_device_data.
                manufacturer_support_fifteen_character_add_device_data[
                'device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(
            manufacturer_support_fifteen_character_add_device_data.
                manufacturer_support_fifteen_character_add_device_data.get('manufacturer'))
        time.sleep(1)
        assert manufacturer_support_fifteen_character_add_device_data.manufacturer_support_fifteen_character_add_device_data.get(
            'device_name') == state_add_device_management_class. \
                   assert_device_name()

        assert manufacturer_support_fifteen_character_add_device_data.manufacturer_support_fifteen_character_add_device_data.get(
            'device_ip') == state_add_device_management_class.assert_device_ip()

        assert manufacturer_support_fifteen_character_add_device_data.manufacturer_support_fifteen_character_add_device_data.get(
            'manufacturer') == state_add_device_management_class.assert_manufacturer()
        # 关闭页面
        state_add_device_management_class.close_web()

