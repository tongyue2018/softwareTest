# @Time : 2020/5/18 10:22 
# @Author : tongyue


'''

python -m pip install pytest-assume

一个方法有多条断言，如果其中1条失败也想继续执行下去，用pytest-assume
'''
import pytest


def test_one():
    print("\n开始------------------")
    pytest.assume(1 == 2)
    pytest.assume(2 == 2)
    pytest.assume(2 == 3)
    print("结束------------------")

if __name__ == '__main__':
    pytest.main(['-sv', 'a-3-plugins-assume.py'])