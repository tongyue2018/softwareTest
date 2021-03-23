# @Time : 2021/3/23 上午10:03 
# @Author : tongyue
import requests

responseObject = requests.put('https://httpbin.org/put',data={'key':'value'})

print(responseObject.json())