# <center>接口自动化测试</center> #
    

### 1.框架基本支持
* 用例编写 pytest
* 执行调度 pytest、pycharm、shell、jenkins
* 测试报告 allure2

### 2.http测试能力
* 请求方法 get、put、post、delete、head
* 执行调度 form、json、xml、binary
* 测试报告 status code、response body、json path、xpath
    
### 3.常见http请求方法构造
* requests.put('https://httpbin.org/put',data={'key':'value'})
* requests.delete('https://httpbin.org/delete')
* requests.head('https://httpbin.org/get')
* requests.options('https://httpbin.org/get')

### 4.演练环境
http://httpbin.testing-studio.com
