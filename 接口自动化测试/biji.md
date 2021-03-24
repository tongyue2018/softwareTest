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

### 5.复杂技术解析
    数据保存：将复杂的xml活着json请求体保存到文件模版中
    
    数据处理：
        * 使用mustache、freemaker等工具解析
        * 简单的字符串替换
        * 使用json(jsonpath) 
        xml(from requests_xml import) XMLSession 
        api进行结构化解析
    
    数据生成：输入最终结果
    
### 6.更多种类断言pyhamcrest
    https://pypi.org/project/PyHamcrest/

### 7.jsonschema
    http://jsonschema.net/
    
### 8.json结构化断言 jsonpath
    jsonpath.jsonpath()
    https://www.jianshu.com/p/cd1552f756ab
    