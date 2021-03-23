# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest
'''
跳过用例
'''

@pytest.mark.skip("无理由放弃用例1")
def test_one():
    print('-----用例1-----')
    assert 5 == 5

def test_two():
    print('-----用例1-----')
    assert 5 == 5

if __name__ == '__main__':
    pytest.main()
