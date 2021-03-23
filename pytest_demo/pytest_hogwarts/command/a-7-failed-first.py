# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''

pytest -s -v a-7-last-failed.py

先执行fail的 再执行其他
pytest -s -v a-7-last-failed.py --failed-first
或者
pytest -s -v a-7-last-failed.py --ff
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
    pytest.main(["-sv", "a-7-last-failed.py", "--failed-first"])