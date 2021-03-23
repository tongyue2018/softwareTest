# @Time : 2020/4/14 17:09 
# @Author : tongyue

'''

pytest-xdist 多CPU分发并行执行用例

python -m pip install pytest-xdist -i  https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

pytest -n 2 a-4-plugins-xdist.py

'''
import pytest


def test_run():
    assert 1==1
def test_bick():
    assert 1==2
if __name__ == '__main__':
    pytest.main(["-sv", "-n 2", "a-4-plugins-xdist.py"])