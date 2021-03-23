# @Time : 2020/4/14 14:38 
# @Author : tongyue
import pytest

test_user_data = ['Tome','Jerry',""]
@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print("打开首页准备登录，登录用户：{}".format(user))
    return user

# indirect=True,表示login_r是个函数，参数test_user_data以此传递给函数

@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print("测试中login的返回值为：{}".format(a))
    assert a != ""

if __name__ == '__main__':
    pytest.main(["-sv", "a-4-parametrize-method.py"])
