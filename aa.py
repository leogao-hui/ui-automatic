#_author:leo gao
#encoding:utf-8

# import exrex
import random
#
# print(exrex.getone(r'(13[0-9]|14[5|7]|15[4]|18[0-9]|17[5-8])(\d{8})'))
# #print(exrex.getone(r'(13[0-9]'))
#
#
# import random

# name = ''
# for i in range(0, 2):
#     name1 = chr(random.randint(0x4e00, 0x9fbf))
#     name += name1
# print(name)

# import random
#
# name = chr(random.randint(65, 90))
# print(name)


filter_add_user_data = {
    'filter_add_user_data_one': {
        'serial_num': '1_filter_serial_number',
        'name': 'filterserialone',
        'account': 'filterone'
    },
    'filter_add_user_data_two': {
        'serial_num': '2_filter_serial_number',
        'name': 'filterserialtwo',
        'account': 'filtertwo'
    },
    'filter_add_user_data_three': {
        'serial_num': '3_filter_serial_number',
        'name': 'filterserialthree',
        'account': 'filterthree'
    },
    'filter_add_user_data_four': {
        'serial_num': '4_filter_serial_number',
        'name': 'filterserialfour',
        'account': 'filterfour'
    },
}

for k in filter_add_user_data:
