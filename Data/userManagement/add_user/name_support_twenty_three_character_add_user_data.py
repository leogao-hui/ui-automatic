#_author:leo gao
#encoding:utf-8

import random

name = ''
for i in range(0, 23):
    name1 = chr(random.randint(0x4e00, 0x9fbf))
    name += name1
account = chr(random.randint(65, 90))

name_support_twenty_three_character_add_user_data = {
    'serial_num': '1_name_support_twenty_three_character',
    'name': name,
    'account': account
    }

