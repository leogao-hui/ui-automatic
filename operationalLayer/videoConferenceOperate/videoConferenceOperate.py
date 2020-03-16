#_author:leo gao
#encoding:utf-8

# import allure
# from Base.base import Base
# from elementLayer.videoCommand.videoCommandElement import VideoCommandElement
# from elementLayer.Login.loginElement import LoginElement
#
#
# class VideoConferenceOperate(Base):
#     def __init__(self, driver, url):
#         super().__init__(driver, url)
#
#     @allure.step('会议创建者登录')
#     def video_command_creator_login(self, account, password, verification_code):
#         self.mandatory_clear(LoginElement.account_input_box)
#         self.mandatory_clear(LoginElement.password_input_box)
#         self.mandatory_clear(LoginElement.verification_code_input_box)
#         self.send_keys(LoginElement.account_input_box, account)
#         self.send_keys(LoginElement.password_input_box, password)
#         self.send_keys(LoginElement.verification_code_input_box, verification_code)
#         self.click(LoginElement.login_confirm_input_box)
#
#     @allure.step('新增视频指挥组')
#     def add_video_command_creator(self, command_group_name):
#         self.click(VideoCommandElement.video_command_button)
#         self.click(VideoCommandElement.add_video_command_group_button)
#         self.send_keys(VideoCommandElement.command_group_name_input_box, command_group_name)
#         self.drop_and_drag()
#         self.click(VideoCommandElement.confirm_button)
#
#     @allure.step('开启视频指挥')
#     def start_video_command(self):
#         self.use_js_click(VideoCommandElement.start_button)
#
#     @allure.step('验证指挥开启')
#     def assert_command_start(self):
#         return self.get_txt_in_tag(VideoCommandElement.assert_command_start)
#
#     @allure.step('验证在线成员直接进入指挥')
#     def assert_online_member_automatic_enter_command(self):
#         return self.get_txt_in_tag(VideoCommandElement.online_automatic_enter_command_member)
#
#     @allure.step('验证上线后成员直接进入指挥')
#     def assert_after_online_automatic_enter_command(self):
#         return self.get_txt_in_tag(VideoCommandElement.after_online_automatic_enter_command_member)
#
#     @allure.step('验证视频')
#     def assert_video(self):
#         return self.get_txt_in_tag(VideoCommandElement.picture_one)
#
#     @allure.step('关闭页面')
#     def close_web(self):
#         self.close()
#
#     @allure.step('拖拽')
#     def drop_and_drag(self):
#         self.drag_and_drop(VideoCommandElement.organization_fifth_account, VideoCommandElement.selected_staff_creator)
#
#     @allure.step('强推成员')
#     def strong_push(self):
#         self.click(VideoCommandElement.online_automatic_enter_command_member)
#         self.click(VideoCommandElement.strong_back_member_button)
#
#     @allure.step('专向指挥')
#     def robert_member(self):
#         self.click(VideoCommandElement.online_automatic_enter_command_member)
#         self.click(VideoCommandElement.perform_the_command_button)
#
#     @allure.step('暂停指挥')
#     def suspended_command(self):
#         self.click(VideoCommandElement.pause_the_command_button)
#
#     @allure.step('退出指挥')
#     def exit_command(self):
#         self.click(VideoCommandElement.exit_the_command_button)
#
#     @allure.step('结束指挥')
#     def end_command(self):
#         self.click(VideoCommandElement.end_the_command_button)



