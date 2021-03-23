# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest
'''
分类运行，有限排序，再执行未排序的
pytest -s a-2-mark-order.py

'''
@pytest.mark.run(order=4)
def test_one():
    print('-----用例1-----')
    assert 5 == 1
@pytest.mark.run(order=3)
def test_two():
    print('-----用例2-----')
    assert 5 == 2
@pytest.mark.run(order=2)
def test_third():
    print('-----用例3-----')
    assert 5 == 4
@pytest.mark.run(order=1)
def test_forth():
    print('\n-----用例4-----')
    assert 5 == 6

def test_fif():
    print('\n-----用例5 未排序-----')
    assert 5 == 6