# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

'''
把一个函数定义为Fixture很简单，只能在函数声明之前加上“@pytest.fixture”。其他函数要来调用这个Fixture，只用把它当做一个输入的参数即可。

yield可以替代return 作为函数的返回值
'''
@pytest.fixture(scope="function")
def before_after():
    # 为什么不会打印呢, 断言失败才会打印出来  可以用 pytest -s 文件名，或者 pytest –-capture=no 文件名
    print('\n调用了我 before')
    yield 3
    print('\n调用了我 after')

def test_one(before_after):
    print('-----------测试用例1-----------')
    assert before_after == 3

def test_two(before_after):
    print('-----------测试用例2----------')
    assert before_after == 5

if __name__ == '__main__':
    pytest.main(['-s', 'a-4-fixtures-yield.py'])