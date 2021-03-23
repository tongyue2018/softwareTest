# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

'''
自动到conftest.py文件找公共模块，数据共享
'''

def test_one(before_after):
    print('-----------测试用例1-----------')
    assert before_after == 3

def test_two(before_after):
    print('-----------测试用例2----------')
    assert before_after == 5

if __name__ == '__main__':
    pytest.main(['-s', 'a-5-fixtures-conftest.py'])