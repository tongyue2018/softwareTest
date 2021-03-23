# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''

pytest -s -v a-12-log.py --resultlog=./log.txt
pytest -s -v a-12-log.py --resultlog=log.txt

'''
import time

import pytest


class TestRun():
    def test_run3(self):
        print("只有run3 测试")
        assert 1 == 2
    def test_run1(self):
        print("只有run1 测试")
        time.sleep(1)
        assert 1 == 1
    def test_run2(self):
        print("只有run2 测试")
        time.sleep(2)
        assert 1 == 2
if __name__ == '__main__':
    pytest.main(["-sv", "a-12-log.py", "--resultlog=./log.txt"])
