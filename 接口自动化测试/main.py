# @Time : 2021/3/23 上午10:03 
# @Author : tongyue
import requests,pytest


def test_get():
        responseObject = requests.get('http://httpbin.testing-studio.com/get',params={'key':'value'})
        assert responseObject.status_code == 200


def test_post():
    responseObject = requests.post('http://httpbin.testing-studio.com/post', data={'key': 'value'})
    assert responseObject.status_code == 200


# 文件上传
# files = {'file':open('report.xls','rb')}
# r = requests.post(url=url,file=files)


if __name__ == '__main__':
    pytest.main(["-sv", "main.py"])