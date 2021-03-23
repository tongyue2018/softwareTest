# @Time : 2020/4/14 16:57 
# @Author : tongyue

'''
丰富的插件

1. pytest-html 生成html报告插件

pip3 install pytest-html
pytest test_reg.py --html=report.html


2.pytest-timeout 限制用例超时时间

pip3 install pytest-timeout
@pytest.mark.timeout(60)
def test_user_reg():  # 当前用例限定60s超时
   ...
或 pytest --timeout=300限定所有用例

3.pytest-rerunfailures 失败重试

pip3 install pytest-rerunfailures
@pytest.mark.flaky(reruns=5, reruns_delay=1)  # 如果失败则延迟1s后重跑
def test_user_reg()  # 最多重跑5次, reruns_delay可以不传
    ....
或pytest --reruns 5 --reruns-delay 1

4.pytest-xdist 多CPU分发并行执行用例

pip3 install pytest-xdist

5.其它
pytest-selenium
pytest-bdd
'''