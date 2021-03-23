# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

'''
把一个函数定义为Fixture很简单，只能在函数声明之前加上“@pytest.fixture”。其他函数要来调用这个Fixture，只用把它当做一个输入的参数即可。

'''
@pytest.fixture()
def before():
    # 为什么不会打印呢, 断言失败才会打印出来  可以用 pytest -s 文件名，或者 pytest –-capture=no 文件名
    print('调用了我 before')
    return 5

def test_one(before):
    assert before == 3

def test_two(before):
    assert before == 4

if __name__ == '__main__':
    pytest.main(['a-1-fixtures-lianxi1.py'])