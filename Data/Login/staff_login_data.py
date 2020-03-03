#_author:leo gao
#encoding:utf-8


admin_account = 'admin'
admin_password = 'admin123'
admin_verification_code = '1111'

add_staff_data = {
    'serial_num': '1',
    'name': 'test',
    'account': 'admintest1'
}

login_staff_data = {
    'staff_account': 'test1',
    'staff_password': 'admin123',
    'staff_verification_code': '1111'
}

reset_password_data = {
    'old_pwd': login_staff_data.get('staff_password'),
    'new_pwd': '19961030gh!!',
    'confirm_pwd': '19961030gh!!'
}

new_login_data = {
    'staff_account': '',
    'staff_password': reset_password_data.get('new_pwd'),
    'staff_verification_code': '1111'
}