# @Time : 2021/3/23 下午9:26 
# @Author : tongyue

# pyhamcrest 支持多种语言

import hamcrest,jsonpath,requests,pytest

def test_json_path():
    responseObject = requests.get('https://home.testing-studio.com/categories.json')
    hamcrest.assert_that(jsonpath.jsonpath(responseObject.json(),'$..name')[0],hamcrest.equal_to('开源项目'))


if __name__ == '__main__':
    pytest.main(["-sv", "hamcrest_test.py"])