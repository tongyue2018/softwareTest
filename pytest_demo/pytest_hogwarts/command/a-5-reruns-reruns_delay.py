# @Time : 2020/4/14 15:13 
# @Author : tongyue
import random
import time
import pytest
'''
用例失败以后重新尝试,
reruns=3 最多重试3次
reruns_delay=1 失败延迟1s后重试

python -m pip install pytest-rerunfailures
@pytest.mark.flaky(reruns=5, reruns_delay=1)  # 如果失败则延迟1s后重跑
def test_user_reg()  # 最多重跑5次, reruns_delay可以不传
    ....
或pytest  -sv a-5-reruns-reruns_delay.py --reruns 5 --reruns-delay 1 
命令行有空格的都要用数组分开 pytest.main(['-sv','a-5-reruns-reruns_delay.py','--reruns','5','--reruns-delay','1'])
'''

# @pytest.mark.flaky(reruns=3,reruns_delay=1)
# def test_one():
#     a = random.randint(3,5)
#     print('a:{}'.format(a))
#     assert a == 4

def test_one():
    a = random.randint(3,5)
    print('a:{}'.format(a))
    assert a == 4
if __name__ == '__main__':
    #命令行有空格的都要用数组分开
    pytest.main(['-sv', 'a-5-reruns-reruns_delay.py', '--reruns', '5', '--reruns-delay', '1'])