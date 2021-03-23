# @Time : 2020/5/18 20:20 
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