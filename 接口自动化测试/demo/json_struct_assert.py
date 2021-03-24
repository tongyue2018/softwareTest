# @Time : 2021/3/23 下午8:50 
# @Author : tongyue

# json结构化断言 json path
import requests,pytest,jsonpath

def test_json():
    responseObject = requests.get('https://home.testing-studio.com/categories.json')
    assert responseObject.json()['category_list']['categories'][0]['name'] == '开源项目'

def test_json_path():
    responseObject = requests.get('https://home.testing-studio.com/categories.json')
    assert jsonpath.jsonpath(responseObject.json(),'$..name')[0] == '开源项目'


if __name__ == '__main__':
    pytest.main(["-sv", "json_struct_assert.py"])