#_author:leo gao
#encoding:utf-8

import pytest
# test_fixture1.py


@pytest.fixture()
def test1():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture(scope='function')
def test2():
    b = '男'
    print('\n传出b')
    return b


def test3(test1):
    name = 'leo'
    print('找到name')
    assert test1 == name


def test4(test2):
    sex = '男'
    print('找到sex')
    assert test2 == sex


if __name__ == '__main__':
    pytest.main(['-s', 'test.py'])