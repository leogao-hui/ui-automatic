#_author:leo gao
#encoding:utf-8

import random

name = chr(random.randint(65, 90)) + chr(random.randint(0x4e00, 0x9fbf))

account_check_again_add_user_data_one = {
    'serial_num': '1_name_check_again',
    'name': name,
    'account': 'account'
}

account_check_again_add_user_data_two = {
    'serial_num': '2_name_check_again',
    'name': '%s哈' % name,
    'account': 'account'
}