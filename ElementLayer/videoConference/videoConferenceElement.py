#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class VideoConferenceElement:

    # 视频会议按钮
    video_conference_button = (By.XPATH, '//div[@class="spsidebar"]/div[2]/button[3]')

    # 新增视频会议按钮
    add_video_conference_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div/button/span')

    # 视频会议组名输入框
    video_conference_name_input_box = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div/div/div[2]/div/input')

    # 新增会议组确定键
    add_video_conference_confirm_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div/div/div[3]/button')

    # 新增会议组取消键
    add_video_conference_cancel_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div/div/div[3]/button[2]')

    # 会议键开始键
    video_conference_start_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div[2]/div[2]/div/div/ul/li/div/button')

    # 会议键编辑键
    video_conference_edit_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div[2]/div[2]/div/div/ul/li/div/button[2]')

    # 会议键删除键
    video_conference_delete_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div[2]/div[2]/div/div/ul/li/div/button[3]')

