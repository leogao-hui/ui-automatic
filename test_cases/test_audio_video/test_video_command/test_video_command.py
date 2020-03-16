#_author:leo gao
#encoding:utf-8

import pytest
import allure
import time
from Data.videoAudio import videoAudioData
from Data.videoAudio.videoAudioData import VideoAudioData


# @allure.feature('视频指挥')
# @pytest.mark.usefixtures('add_user')
# class TestVideoCommand:
#
#     @allure.story('这是一个测试单个人开视频指挥的case')
#     def test_one_people_start_video_command(self, command_class):
#         command_class.video_command_creator_login(VideoAudioData.user_data['user_one']['account'],
#                                                   VideoAudioData.user_data['user_one']['new_pwd'],
#                                                   VideoAudioData.user_data['user_one']['verification_code'])
#         command_class.add_video_command_creator(VideoAudioData.video_command_name)
#         command_class.start_video_command()
#         assert 'userone' in command_class.assert_command_start()
#         command_class.close_web()
#
#     @allure.story('这是一条测试指挥正常开启后，在线的成员直接进入到指挥的case')
#     def test_online_member_direct_access_to_command(self, command_class):
#         assert 'usertwo' in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条测试指挥正常开启后，在线的非成员没有进入到指挥中的case')
#     def test_not_online_member_not_access_to_command(self, command_class):
#         assert 'usertwo' not in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条测试指挥正常开启后，不在线的成员上线后自动加入，正常加入')
#     def test_not_online_member_after_online_add_automatically(self, command_class):
#         assert 'userthree' in command_class.assert_after_online_automatic_enter_command()
#
#     @allure.story('这是一条指挥正常开启后，不在线的非成员上线后不会自动加入的case')
#     def test_not_online_not_member_not_add_automatically(self, command_class):
#         assert 'userthree' not in command_class.assert_after_online_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，任意成员正常查看所有成员等级和名称的case')
#     def test_any_member_view_all_member_name_level(self, command_class):
#         assert 'usertwo' in command_class.assert_online_member_automatic_enter_command()
#         assert 'userthree' in command_class.assert_after_online_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，任意成员正常查看和收听上一级和下一级的音视频')
#     def test_any_member_view_low_level_superior_audio_and_video(self, command_class):
#         assert 'data:image/png;base64' in command_class.assert_video()
#
#     @allure.story('这是一条指挥开启后，成员状态为在线，离线，专向中，协同中，越级中，授权中，接替中的case')
#     def test_member_status_online_not_online_perform(self, command_class):
#         assert 'usertwo' in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，创建者添加一个未被用户绑定的设备，正常添加的case')
#     def test_creator_add_device_not_bind_user_success(self, command_class):
#         assert 'deviceone' in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，创建者添加一个被用户绑定的设备，报错不能添加的case')
#     def test_creator_add_device_bind_user_error(self, command_class):
#         assert 'deviceone' not in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条指挥结束后，被添加的成员不在指挥组中的case')
#     def test_command_end_member_added_not_in_command_group(self, command_class):
#         assert 'usertwo' in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条创建者正常强退直属下级成员，被强退的成员状态变为离线，等级不变的case')
#     def test_strong_back_directly_under_member(self, command_class):
#         command_class.strong_push()
#         assert 'userfour' in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条任意成员强退上级成员，报错的case')
#     def test_strong_back_superior_member_error(self, command_class):
#         command_class.strong_push()
#         assert 'usefour' not in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，上级成员专向指挥非直属下级，报错的case')
#     def test_strong_back_not_directly_under_member_error(self, command_class):
#         command_class.robert_member()
#         assert 'userthree' not in command_class.assert_online_member_automatic_enter_command()
#
#     @allure.story('这是一条指挥开启后，指挥组创建者暂停指挥，可以退出指挥的case')
#     def test_creator_suspend_command_can_exit_command(self, command_class):
#         command_class.suspended_command()
#         command_class.exit_command()
#         assert '' in command_class.assert_online_member_automatic_enter_command
#
#     @allure.story('这是一条指挥开启后，指挥组创建者或暂停指挥，可以结束指挥的case')
#     def test_creator_suspend_command_can_end_command(self, command_class):
#         command_class.suspended_command()
#         command_class.end_command()
#         assert '' in command_class.assert_online_member_automatic_enter_command
#
#     @allure.story('这是一条指挥开启后，创建者要人关闭 循环100次的case')
#     def test_creator_start_invite_end_cycle_one_hundred(self, command_class):
#         for i in range(100):
#             command_class.start_video_command()
#             command_class.end_command()
#         assert '' in command_class.assert_online_member_automatic_enter_command
#
#     @allure.story('这是一条指挥开启后，循环强退邀请人员的case')
#     def test_cycle_strong_back_invite_member(self, command_class):
#         for i in range(100):
#             command_class.strong_push()
#             command_class.start_video_command()
#         assert 'userone' in command_class.assert_online_member_automatic_enter_command








