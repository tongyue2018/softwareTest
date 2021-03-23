# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest
'''
跳过用例
'''
a=2
b=3
@pytest.mark.skipif() #无条件跳过
def test_one():
    print('-----用例1-----')
    assert 5 == 5
@pytest.mark.skipif(reason="无理由跳过") #无条件跳过，写上reason
def test_two():
    print('-----用例1-----')
    assert 5 == 5

@pytest.mark.skipif(a < b, reason="无理由跳过") #有条件跳过，要写上reason
def test_third():
    print('-----用例1-----')
    assert 5 == 5