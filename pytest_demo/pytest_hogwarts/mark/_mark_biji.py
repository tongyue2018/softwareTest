# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest


'''
mark主要用来标记用例,通过不同的标记实现不同的运行策略
主要用途:

1.标记和分类用例: @pytest.mark.level1

2.标记用例执行顺顺序pytest.mark.run(order=1) (需安装pytest-ordering)

3.标记使用指定fixture(测试准备及清理方法) @pytest.mark.usefixtures()

4.参数化 @pytest.mark.parametrize

5.标记超时时间 @pytest.mark.timeout(60) (需安装pytest-timeout)

6.标记失败重跑次数@pytest.mark.flaky(reruns=5, reruns_delay=1) (需安装pytest-rerunfailures)

7.标记用例在指定条件下跳过或直接失败 @pytest.mark.skipif()/xfail()


'''
