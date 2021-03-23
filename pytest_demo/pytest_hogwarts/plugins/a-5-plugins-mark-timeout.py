# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest
'''
设置超时时间,如果超时，则不会执行下面的用例
python -m pip install pytest-timeout
@pytest.mark.timeout(60)
def test_user_reg():  # 当前用例限定60s超时
   ...
或 pytest --timeout=300限定所有用例

'''
a=2
b=3
@pytest.mark.timeout(1)
def test_one():
    print('-----用例1-----')
    time.sleep(0.5)
    assert 5 == 5

@pytest.mark.timeout(1)
def test_two():
    print('-----用例2-----')
    time.sleep(1.5) # 报timeout异常了
    assert 5 == 5

def test_third():
    print('-----用例3-----')
    assert 5 == 5
if __name__ == '__main__':
    pytest.main(['-s', 'a-5-plugins-mark-timeout.py'])