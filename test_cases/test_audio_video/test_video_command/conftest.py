#_author:leo gao
#encoding:utf-8


import pytest
from operationalLayer.videoCommand.videoCommandOperate import VideoCommandOperate
from Url.videoCommand.videoCommand import video_command_url


@pytest.fixture()
def command_class(state_driver):
    command_operate = VideoCommandOperate(state_driver, video_command_url)
    return command_operate

