# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''
总数失败1次后退出（失败）
pytest -s a-6-maxfail.py   --maxfail=1
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
    pytest.main(["-s", "a-6-maxfail.py", "--maxfail=1"])