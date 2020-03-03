#_author:leo gao
#encoding:utf-8

import random
import exrex
account = chr(random.randint(65, 90)) + exrex.getone(r'(13[0-9]|14[5|7]|15[4]|18[0-9]|17[5-8])(\d{8})')
name = chr(random.randint(65, 90))

account_support_chinese_english_add_user_data = {
    'serial_num': '1accountr',
    'name': name,
    'account': account
}