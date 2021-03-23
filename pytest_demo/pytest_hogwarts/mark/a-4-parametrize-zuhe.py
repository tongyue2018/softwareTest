# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

#参数化
#onData要保持一致
#多个参数接受数据，将listData展开传递给oneData，listData有多少个就会执行多少此次

data_1 = [1, 2]
data_2 = [2, 4]

@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    assert a==b


if __name__ == '__main__':
    pytest.main(['-sv', 'a-4-parametrize-zuhe.py'])