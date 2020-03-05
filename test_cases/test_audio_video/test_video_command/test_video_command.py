#_author:leo gao
#encoding:utf-8

import pytest
import allure
import time
from Data.videoAudio import videoAudioData


@allure.feature('视频指挥')
@pytest.mark.usefixtures('add_user')
class TestVideoCommand:

    @allure.story('这是一个测试单个视频指挥的case')
    def test_normal_add_device(self):
        pass