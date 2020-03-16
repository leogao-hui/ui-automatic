#_author:leo gao
#encoding:utf-8

import pytest
import time
from operationalLayer.Login.login import LoginOperate
from operationalLayer.deviceManagement.deviceManagementAddOperate import DeviceManagementAddOperate
from operationalLayer.userManagement.userManagementAddOperate import UserManagementAddOperate
from Url.userManagement import userManagement
from Url.deviceManagement import deviceManagement
from Url.Login import login
from Data.Login import noraml_login_data
from Data.videoAudio import videoAudioData


@pytest.fixture()
def state_login_class(state_driver):
    login_operate = LoginOperate(state_driver, login.login_url)
    return login_operate


@pytest.fixture()
def state_add_device_management_class(state_driver):
    add_device_management_operate = DeviceManagementAddOperate(state_driver, deviceManagement.device_manager_url)
    return add_device_management_operate


@pytest.fixture()
def state_add_user_management_class(state_driver):
    add_user_management_operate = UserManagementAddOperate(state_driver, userManagement.user_manager_url)
    return add_user_management_operate


@pytest.fixture()
def add_user(state_login_class, state_add_user_management_class):
    for key in videoAudioData.VideoAudioData.user_data:
        state_login_class.get_login_url()
        state_login_class.clear_data()
        state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                        noraml_login_data.verification_code)
        state_login_class.confirm_login_button()
        state_add_user_management_class.click_user_management()
        state_add_user_management_class.add_user(videoAudioData.VideoAudioData.user_data[key]['serial_num'],
                                                 videoAudioData.VideoAudioData.user_data[key]['name'],
                                                 videoAudioData.VideoAudioData.user_data[key]['account'])
        state_add_user_management_class.choose_organization()
        time.sleep(1)
        state_add_user_management_class.confirm()
        #state_login_class.cancellation_account()

        # 重置密码
        state_login_class.get_login_url()
        state_login_class.clear_data()
        state_login_class.input_account(videoAudioData.VideoAudioData.user_data[key]['account'],
                                        videoAudioData.VideoAudioData.user_data[key]['old_pwd'],
                                        videoAudioData.VideoAudioData.user_data[key]['verification_code'])
        state_login_class.confirm_login_button()
        state_login_class.reset_password(videoAudioData.VideoAudioData.user_data[key]['old_pwd'],
                                         videoAudioData.VideoAudioData.user_data[key]['new_pwd'],
                                         videoAudioData.VideoAudioData.user_data[key]['new_pwd'])


@pytest.fixture()
def add_device(state_login_class, state_add_device_management_class):
    for key in videoAudioData.VideoAudioData.device_data:
        state_login_class.get_login_url()
        state_login_class.clear_data()
        state_login_class.input_account(noraml_login_data.account, noraml_login_data.password,
                                        noraml_login_data.verification_code)
        state_login_class.confirm_login_button()
        state_add_device_management_class.click_device_management()
        state_add_device_management_class.input_device_name_ip(videoAudioData.VideoAudioData.
                                                               device_data[key]['device_name'],
                                                               videoAudioData.VideoAudioData.device_data[key]['device_ip'])
        state_add_device_management_class.choose_device_type()
        state_add_device_management_class.choose_organization_manufacturer(videoAudioData.
                                                                           VideoAudioData.device_data[key]['manufacturer'])



