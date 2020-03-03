#_author:leo gao
#encoding:utf-8


import random

name = chr(random.randint(65, 90))
account = chr(random.randint(65, 90))

account_not_support_special_characters_add_user_data = {
    'serial_num': '1_account_not_support_special_characters',
    'name': name,
    'account': '#%s' % account
}