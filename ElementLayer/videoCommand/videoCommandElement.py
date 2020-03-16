#_author:leo gao
#encoding:utf-8

from selenium.webdriver.common.by import By


class VideoCommandElement:

    # 视频指挥按钮
    video_command_button = (By.XPATH, '//div[@class="spsidebar"]/div[2]/button[2]')

    # 新建视频指挥组按钮
    add_video_command_group_button = (By.XPATH, '//div[@class="spsidebar"]/div[3]/div/div/button/span')

    # 指挥组名输入框
    command_group_name_input_box = (By.XPATH, '//div[@class="spzhside"]/div/div/div[2]/div/input')

    # 组织结构按钮
    structure_of_the_organization_button = (By.XPATH, '//div[@class="spzhside"]/div/div/div[2]/div[2]div[2]/div/button')

    # 设备资源按钮
    device_resource_button = (By.XPATH, '//div[@class="spzhside"]/div/div/div[2]/div[2]div[2]/div/button[2]')

    # 关键字搜索
    keyword_search_input_box = (By.XPATH, '//div[@class="spzhside"]/div/div/div[2]/div[2]div[2]/div[2]/input')

    # 确定键
    confirm_button = (By.XPATH, '//div[@class="spzhside"]/div/div/div[3]/button')

    # 取消键
    cancel_button = (By.XPATH, '//div[@class="spzhside"]/div/div/div[3]/button[2]')

    # 启动按钮
    start_button = (By.XPATH, '//div[@class="spzhside"]/div[2]/div[2]/div/div/ul/li/div/button[1]')

    # 编辑按钮
    edit_button = (By.XPATH, '//div[@class="spzhside"]/div[2]/div[2]/div/div/ul/li/div/button[2]')

    # 删除按钮
    delete_button = (By.XPATH, '//div[@class="spzhside"]/div[2]/div[2]/div/div/ul/li/div/button[3]')

    # 添加成员按钮
    add_member_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button')

    # 强退成员按钮
    strong_back_member_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[2]')

    # 授权指挥
    authorization_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[3]')

    # 协同指挥
    coordinated_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[4]')

    # 专向指挥
    perform_the_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[5]')

    # 越级指挥
    great_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[6]')

    # 接替指挥
    replace_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[7]')

    # 对下静默
    to_the_silent_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[8]')

    # 对上静默
    on_the_silent_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[9]')

    # 退出指挥
    exit_the_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[10]')

    # 暂停指挥
    pause_the_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[11]')

    # 结束指挥
    end_the_command_button = (By.XPATH, '//div[@class="spzhside"]/div[4]/div[3]/button[12]')

    # 验证指挥开始
    assert_command_start = (By.XPATH, '//div[@class="zhz-tree"]/div/div/div/div[2]/li/div/span/span/span')

    # 第一个账号
    organization_first_account = (By.XPATH, '//div[@class="treebox"]/div/div/div/div/div/li/ul/div[1]/li/div/span/span/span')

    # 第二个账号
    organization_second_account = (By.XPATH, '//div[@class="treebox"]/div/div/div/div/div/li/ul/div[2]/li/div/span/span/span')

    # 第三个账号
    organization_third_account = (By.XPATH, '//div[@class="treebox"]/div/div/div/div/div/li/ul/div[3]/li/div/span/span/span')

    # 第四个账号
    organization_fourth_account = (By.XPATH, '//div[@class="treebox"]/div/div/div/div/div/li/ul/div[4]/li/div/span/span/span')

    # 第五个账号
    organization_fifth_account = (By.XPATH, '//div[@class="treebox"]/div/div/div/div/div/li/ul/div[5]/li/div/span/span/span')

    # 已选人员创建者
    selected_staff_creator = (By.XPATH, '//div[@class="peopletree"]/div/div/div/div/li/ul/div/li/div/span/span/span')

    # 在线自动进入成员
    online_automatic_enter_command_member = (By.XPATH, '//div[@class="zhz-tree"]/div/div/div/div[2]/li/ul/div/li/div/span[3]/span/span')

    # 上线后自动加入成员
    after_online_automatic_enter_command_member = (By.XPATH, '//div[@class="zhz-tree"]/div/div/div/div[2]/li/ul/div/li/div/span/span/span')

    # 画面一
    picture_one = (By.XPATH, '//div[@id="app"]/div[3]/div[2]/div/div[3]/div/div/div[2]/div[3]/img')

