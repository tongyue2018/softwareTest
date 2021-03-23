# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''
包含run1或者run2的用例
pytest -sv  a-4-k.py

-s 表示打印print对应的log信息，
    或者logging的log信息(如果不加s，则用例执行错误的时候才打印log 执行正确的情况不打印log)
-v 详细的执行结果，细化到每个函数

'''
import pytest


class TestRun():
    def test_run1(self):
        print("只有run1 测试")
        assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-sv', 'a-4-sv.py'])


