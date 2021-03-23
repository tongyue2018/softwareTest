# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest


'''
fixture 得一个optional的参数是autouse, 默认设置为False。
当默认为False，就可以选择用上面两种方式来试用fixture。
当设置为True时，在一个session内的所有的test都会自动调用这个fixture。
权限大，责任也大，所以用该功能时也要谨慎小心。

fixture scope：
function：每个test都运行，默认是function的scope
class：每个class的所有test只运行一次
module：每个module的所有test只运行一次
session：每个session只运行一次
'''
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('-----------------')

@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')

def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')

if __name__ == '__main__':
        pytest.main(["-sv", "a-2-fixtures-lianxi2.py"])
