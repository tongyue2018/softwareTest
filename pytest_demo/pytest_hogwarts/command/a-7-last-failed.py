# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''

pytest -s -v a-7-last-failed.py

执行上次失败的用例
pytest -s a-7-last-failed.py  --last-failed
或者
pytest -s a-7-last-failed.py  --lf
'''
import pytest


class TestRun():
    def test_run1(self):
        print("只有run1 测试")
        assert 1 == 1
    def test_run2(self):
        print("只有run2 测试")
        assert 1 == 2
if __name__ == '__main__':
    pytest.main(["-sv", "a-7-last-failed.py", "--last-failed"])