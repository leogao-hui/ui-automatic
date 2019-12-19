#_author:leo gao
#encoding:utf-8

from selenium import webdriver
import unittest
from OperationalLayer.Login.login import LoginOperate
from Data.Login import noraml_login_data
from Utils.operateDatabaseData import delete_database_data_test_ci, add_database_data_test_ci
from Url.Login import login


class TestSearchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        delete_database_data_test_ci()
        add_database_data_test_ci()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Login_operate = LoginOperate(self.driver, login.login_url)

    def test_normal_login(self):
        self.Login_operate.get_url()
        self.Login_operate.input_account(noraml_login_data.account, noraml_login_data.password,
                                         noraml_login_data.verification_code)
        self.Login_operate.confirm_login_button()

