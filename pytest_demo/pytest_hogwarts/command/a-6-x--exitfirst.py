# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''
首次失败就退出 -x或者--exitfirst
pytest -s  a-6-x--exitfirst.py  --exitfirst
或者
pytest -s -x a-6-x--exitfirst.py

'''
import pytest


class TestRun():
    def test_run1(self):
        print("只有run1 测试")
        assert 1 == 2
    def test_run2(self):
        print("只有run2 测试")
        assert 1 == 2
if __name__ == '__main__':
    pytest.main(["-s", "a-6-x--exitfirst.py", "--exitfirst"])