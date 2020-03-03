#_author:leo gao
#encoding:utf-8

import random

name = chr(random.randint(65, 90)) + chr(random.randint(0x4e00, 0x9fbf))
account = chr(random.randint(65, 90))

name_support_chinese_english_add_user_data = {
    'serial_num': '1namesupportchinese',
    'name': name,
    'account': 'account%s' % account
}