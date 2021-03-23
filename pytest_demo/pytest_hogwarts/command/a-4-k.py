# @Time : 2020/4/15 8:31 
# @Author : tongyue

'''
包含run1或者run2的用例
pytest -svk "test_run1 or test_go1" a-4-k.py

包含run的用例
pytest -svk "run" a-4-k.py

不包含run的用例
pytest -svk "not run" a-4-k.py

--and  2个关键字都包含，比如test_go_two
pytest -svk "go and two" a-4-k.py

'''
import pytest


class TestRun():
    def test_run1(self):
        print("只有run1 测试")
        assert 1 == 1

    def test_run2(self):
        print("只有run2 测试")
        assert 3 == 2

class TestGo():
    def test_go1(self):
        print("只有go1 测试")
        assert 1 == 1

    def test_go_two(self):
        print("只有go2 测试")
        assert 1 == 2
if __name__ == '__main__':
    # pytest.main(['-svk','test_run1 or test_go1','a-4-k.py'])
    # pytest.main(['-svk', 'run', 'a-4-k.py'])
    # pytest.main(['-svk', 'not run', 'a-4-k.py'])
    pytest.main(['-svk', 'go and two', 'a-4-k.py'])


