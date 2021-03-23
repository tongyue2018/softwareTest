# @Time : 2020/4/14 15:13 
# @Author : tongyue

import time
import pytest
'''
分类运行
pytest -m "demo1" a-1-mark-m-biaoji.py

pytest -m "demo1 or demo2"  a-1-mark-m-biaoji.py

有warnnig警告信息，则在conftest.py加入对应代码即可，见conftest.py第二段代码

'''
@pytest.mark.demo1
def test_one():
    assert 5 == 1
@pytest.mark.demo1
def test_two():
    assert 5 == 2

@pytest.mark.demo2
def test_three():
    assert 5 == 4

@pytest.mark.demo3
def test_fore():
    assert 5 == 5

if __name__ == '__main__':
    pass
    # pytest.main(['-sv','a-1-mark-m-biaoji.py','-m','demo1', 'or', 'demo2'])