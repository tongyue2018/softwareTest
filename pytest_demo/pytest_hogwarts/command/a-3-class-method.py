# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''
只跑某个类中的某个方法
pytest -s a-3-class-method.py::TestGo::test_go1

'''
import pytest


class TestRun():
    def test_run1(self):
        assert 1 == 1

    def test_run2(self):
        assert 1 == 2

class TestGo():
    def test_go1(self):
        print("只有go1 测试")
        assert 1 == 1

    def test_go2(self):
        assert 1 == 2
if __name__ == '__main__':
     pytest.main(["-s", "a-3-class-method.py::TestGo::test_go1"])