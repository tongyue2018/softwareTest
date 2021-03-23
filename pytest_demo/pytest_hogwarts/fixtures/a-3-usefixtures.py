# @Time : 2020/4/15 11:30 
# @Author : tongyue
import pytest

'''
当用例需要调用fixture时，前面讲到可以直接在用例里加fixture参数，如果一个测试class都需要用到fixture，每个用例都去传参，会比较麻烦，这个时候，
可以在class外面加usefixtures装饰器，让整个class都调用fixture

usefixtures缺点：不能使用函数的返回值

调用fixture的三种方法（本地用方法2）
1.函数或类里面方法直接传fixture的函数名称
2.使用装饰器@pyets.mark.usefixtures()修饰  
3.autouse=True自动使用

 @pytest.mark.usefixtures("fixture1","fixture2")
 
 pytest -sv a-3-usefixtures.py
 
'''

@pytest.fixture(scope='class')
def start():
    print("\n--开始测试了：start-------------")
    yield 1
    print("\n--结束测试了：finish-------------")

@pytest.mark.usefixtures("start")
class TestDo():
    def test_run1(self):
        print("run1 test")
        assert start==1
    def test_run2(self):
        print("run2 test")
        assert 1 == 1

if __name__ == '__main__':
    pytest.main(["-s", "a-3-usefixtures.py"])