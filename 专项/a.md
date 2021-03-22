<br/>
# <center>django遇到的问题</center> #
<br/>

1.django.core.exceptions.ImproperlyConfigured: SQLite 3.8.3 or later is required

    https://blog.csdn.net/szuhuanggang/article/details/89555319

    查找django安装目录：
    cd /
    find -name django
    然后发现相关目录：
    
    ./usr/local/lib/python3.6/site-packages/django
    ./usr/local/lib/python3.6/site-packages/django/forms/jinja2/django
    ./usr/local/lib/python3.6/site-packages/django/forms/templates/django
    修改sqlite的base.py：
    
    vi /usr/local/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py
    注释掉抛出异常语句（然后提示expected an indented block，所有随便加了一条语句，构成一个block）：
    vim /root/.virtualenvs/py36env/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py

    def check_sqlite_version():
	    pass
	    #if Database.sqlite_version_info < (3, 8, 3):
	    #raise ImproperlyConfigured('SQLite 3.8.3 or later is required (found %s).' % Database.sqlite_version)

2.linux启动后，通过域名访问报错

    Invalid HTTP_HOST header: ‘xxx.xx.xxx.xxx:8000’. You may need to add ‘xxx.xx’ to ALLOWED_HOSTS

    解决办法： 
    修改创建项目时生成的setting.py文件将
    ALLOWED_HOSTS = [] 改为
    ALLOWED_HOSTS = ['*']
    再次运行即可成功访问。

3.

    Starting development server at http://0.0.0.0:8000/

4.uwsgi 安装报错

    yum install -y libffi libffi-devel
    yum install -y libssl  libssl-dev

    1.可以先查看一下含python-devel的包
    yum search python | grep python-devel
    2.64位安装python-devel.x86_64，32位安装python-devel.i686，我这里安装:
    sudo yum install python-devel.x86_64

    最后看的菜鸟教程
    yum groupinstall "Development tools"
    yum install zlib-devel bzip2-devel pcre-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel
    
	yum search python36 | grep python-devel
	挨个安装，这下OK了
    

    uwsgi --ini /etc/uwsgi8000.ini &
    /usr/local/nginx/sbin/nginx
    
5.配置uwsgi
    nginx: [emerg] unknown directive "//必须和uwsgi中的设置一致" in /usr/local/nginx/conf/nginx.conf:114

	花了大半天，最后是复制代码惹的祸，//在nginx里面不是注释 要用 #号，否则报错

6.测试 uwsgi --http :8001 --wsgi-file test.py


    原因：测试用例对于python2.x 和 python3.x的写法不同。 
    python2.x请用一下用例测试：
    
    def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
    
    python3.x请用一下用例测试：
    
    def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
    
7.
    ==> error.log <==
    2019/05/02 22:02:55 [error] 28937#0: *297 connect() failed (111: Connection refused) while connecting to upstream, client: 116.77.72.5, server: extiger.com, request: "GET / HTTP/1.1", upstream: "uwsgi://127.0.0.1:9090", host: "47.107.58.164"
    
    找到原因： 吐血，django没启动...，以为配置完成是自动启动的
    django-admin startproject HelloWorld


8.ng报错503 502，django也有日志，都通了,很奇怪的502

    找到原因：网页地址端口写错了，要写uwsgi配置的端口（或nginx location配置的端口），不是nginx  lister的端口

9.http完成，再玩https

    you're accessing the development server over HTTPS, but it only supports HTTP
	
	pip install django-sslserver #根本解决的地方
    pip install django-extensions
    pip install django-werkzeug-debugger-runserver
    pip install pyOpenSSL
    
    修改setting.py文件
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    
    'werkzeug_debugger_runserver', #增加部分
    'django_extensions',#增加部分,
	'sslserver',#增加部分 根本解决了问题
    ]

    &表示后台运行，nohup不中断，日志自动保存到 nohup.out（有manage.py同级）
	nohup python manage.py runsslserver  0.0.0.0:9090 \
    --certificate /env/nginx/conf/cert/2137784_extiger.com.pem \
    --key /env/nginx/conf/cert/2137784_extiger.com.key &




10.uwsgi django多站点

    启动2个uwsgi， nginx配置多个server即可
    http://www.cnblogs.com/pythonClub/p/9827225.html

11.调试模式
    
    1.如果开启了DEBUG模式，那么以后我们修改了Django项目的代码，然后按下ctrl+s，那么Django就会自动的给我们重启项目，不需要手动重启。
    2.如果开启了DEBUG模式，那么以后Django项目中的代码出现bug了，那么在浏览器中和控制台会打印出错信息。否则的我们很难寻找到bug的位置，也不方便调试代码。
    在生产环境中，禁止开启DEBUG = True，因为当你的网站出错误时，别人能看到你的源代码，而我们也不需要给用户看到这些错误信息。所以需要关掉DEBUG = True，即设置DEBUG = False
    如果设置了DEBUG = False，那么就必须设置settings.py中的ALLOWED_HOSTS.
    ALLOWED_HOSTS：这个变量是用来设置以后别人只能通过这个变量中的ip地址或者域名来进行访问。
    不知道ALLOWED_HOSTS的可以参考一下我前面一片博客。https://blog.csdn.net/xujin0/article/details/83189156

12.debug模式 DEBUG = False的时候，404

    部署正式项目，自动解决了。。。
    一般配置DEBUG = False  ALLOWED_HOSTS = ['*']
    以及第16条解决方案

13.http重定向到https -- 未解决

    阿里云 不让访问80端口，奇怪直接访问http 很久后超时，提示连接重置，按下回车以后才定向到https,应该是谷歌浏览器的操作，总之没有直接定向到https

14.www.访问不了，去掉www.可以访问 -- 未解决


15.手机访问不了域名 -- 未解决


16.html部署到django项目后，无法引用js css image


    https://blog.csdn.net/zxyhfdl/article/details/81907021

17.部署css js 如何更新浏览器缓存