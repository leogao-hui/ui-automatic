#_author:leo gao
#encoding:utf-8

import pytest
import allure
import time
from Data.videoAudio import videoAudioData
from Data.videoAudio.videoAudioData import VideoAudioData


# @allure.feature('视频会议')
# @pytest.mark.usefixtures('add_user')
# class TestVideoConference:
#
#     @allure.story('这是一个测试单个人开视频会议的case')
#     def test_one_people_start_video_conference(self, conference_class):
#         conference_class.video_command_creator_login(VideoAudioData.user_data['user_one']['account'],
#                                                   VideoAudioData.user_data['user_one']['new_pwd'],
#                                                   VideoAudioData.user_data['user_one']['verification_code'])
#         conference_class.add_video_command_creator(VideoAudioData.video_command_name)
#         conference_class.start_video_command()
#         assert 'userone' in conference_class.assert_command_start()
#         conference_class.close_web()
#
#     @allure.story('这是一个创建者和5个人正常开启会议的case')
#     def test_one_creator_five_people_start_video_conference(self, conference_class):
#         conference_class.start_video_command()
#         assert 'userone' in conference_class.assert_command_start()
#         conference_class.close_web()
#
#     @allure.story('这是一个会议正常开启后，在线的成员直接进入到会议的case')
#     def test_online_member_in_meeting_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一个会议正常开启后，在线的非成员没有进入到会议中的case')
#     def test_online_not_member_not_in_meeting_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一个会议正常开启后，不在线的成员上线后自动加入，正常加入的case')
#     def test_offline_member_after_online_in_meeting_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一个会议正常开启后，不在线的非成员上线后不会自动加入的case')
#     def test_offline_not_member_after_online_not_in_meeting_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，创建者添加一个未被用户绑定的设备，正常添加的case')
#     def test_creator_normal_add_device_not_bind_people_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，创建者添加一个被用户绑定的设备，报错不能添加的case')
#     def test_creator_error_add_device_bind_people_after_start_the_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议结束后，被添加的成员不在会议组中的case')
#     def test_added_member_not_in_conference_group_after_end_the_meeting(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，创建者正常强退直属下级成员的case')
#     def test_creator_strong_back_directly_under_the_lower(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，任意成员强退上级成员，报错的case')
#     def test_any_people_strong_back_immediate_superior(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，成员主动退出，状态变为离线的case')
#     def test_member_take_the_initiative_to_quit_status_is_offline_after_conference_start(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，指挥组创建者暂停会议，可以退出会议的case')
#     def test_creator_suspended_conference_quit_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一条.会议开启后，指挥组创建者或最高级成员暂停会议，可以结束会议的case')
#     def test_creator_suspended_conference_end_conference(self, conference_class):
#         pass
#
#     @allure.story('这是一条会议开启后，创建者邀人关闭循环100次的case')
#     def test_creator_start_invite_end_cycle_one_hundred(self, conference_class):
#         pass