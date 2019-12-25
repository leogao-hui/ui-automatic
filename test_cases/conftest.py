#_author:leo gao
#encoding:utf-8

import pytest
from Utils.operateDatabaseData import delete_database_data_test_ci, add_database_data_test_ci


@pytest.fixture(scope='class', autouse=True)
def database_base_configuration():
    delete_database_data_test_ci()
    add_database_data_test_ci()

