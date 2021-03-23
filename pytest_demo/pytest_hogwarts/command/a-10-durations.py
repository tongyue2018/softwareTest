# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''

pytest -s -v a-10-durations.py

显示执行最慢的2条用例（所有都会执行，只是最慢的会单独列出, 在控制台打印了，没有在报告中显示）
pytest -s -v a-10-durations.py --durations=2 --html=report.html

=========================================================================================== slowest 2 test durations ============================================================================================
2.00s call     a-10-durations.py::TestRun::test_run2
1.00s call     a-10-durations.py::TestRun::test_run1


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
    pytest.main(["-sv", "a-10-durations.py", "--durations=2"])