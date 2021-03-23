# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

'''
1.fixture是pytest的一个闪光点，fixture是pytest特有的功能，它用pytest.fixture标识，定义在函数前面。在你编写测试函数的时候，
你可以将此函数名称做为传入参数，pytest将会以依赖注入方式，将该函数的返回值作为测试函数的传入参数。

2.fixture有明确的名字，在其他函数，模块，类或整个工程调用它时会被激活。

3.fixture是基于模块来执行的，每个fixture的名字就可以触发一个fixture的函数，它自身也可以调用其他的fixture。

4.fixture主要的目的是为了提供一种可靠和可重复性的手段去运行那些最基本的测试内容。比如在测试网站的功能时，每个测试用例都要登录和退出，
利用fixture就可以只做一次，否则每个测试用例都要做这两步也是冗余。


当用例需要调用fixture时，前面讲到可以直接在用例里加fixture参数，如果一个测试class都需要用到fixture，每个用例都去传参，会比较麻烦，这个时候，
可以在class外面加usefixtures装饰器，让整个class都调用fixture

调用fixture的三种方法
1.函数或类里面方法直接传fixture的函数名称
2.使用装饰器@pyets.mark.usefixtures()修饰
3.autouse=True自动使用

'''

