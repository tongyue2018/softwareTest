# @Time : 2020/4/15 8:26 
# @Author : tongyue

import pytest
def test_run1():
    assert 7==8

if __name__ == '__main__':
     pytest.main(["-s", "nottest.py"])