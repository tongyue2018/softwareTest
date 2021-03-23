# @Time : 2020/4/14 16:57 
# @Author : tongyue

'''
丰富的插件

1. pytest-html 生成html报告插件

python -m pip install pytest-html -i  https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pytest a-1-plugins-html.py --html=report.html
pytest a-1-plugins-html.py --html=report.html  --self-contained-html
'''

import pytest


def test_run():
    assert 1==1
def test_bick():
    assert 1==2
if __name__ == '__main__':
    pytest.main(["-s", "a-1-plugins-html.py", "--html=report.html"])