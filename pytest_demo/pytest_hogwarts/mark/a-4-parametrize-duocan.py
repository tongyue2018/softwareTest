# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

#参数化
#onData要保持一致
#多个参数接受数据，将listData展开传递给oneData，listData有多少个就会执行多少此次
listData = [[1,2,3],[4,5,6]]


@pytest.mark.parametrize('oneData,twoData,result', listData)
class TestCase():

    def test_one(self,oneData,twoData,result):
        assert (oneData+twoData) == result
if __name__ == '__main__':
    pytest.main(["-s", "a-4-parametrize-duocan.py"])