# @Time : 2020/4/14 16:54 
# @Author : tongyue

'''

灵活的运行控制,通过pytest ...命令,可以实现非常灵活的执行控制

1.运行目录及子包下的所有用例: pytest 目录名

2.运行指定模块所有用例: pytest test_reg.py

3.pytest test_reg.py::TestClass::test_method 运行指定模块指定类指定用例

4.运行名称包含指定表达式的用例：-k 表达式(支持and or not),如pytest -k "test_a and test_b" --  过滤关键字

5.运行指定标签(mark)的用例： -m 标签(支持and or not), 如pytest -m "apitest and level1"

6.遇到失败后停止：--exitfirst 首次失败后退出(可用于保留出错现场)  --maxfail=3 3次失败后退出 表示用例失败总数等于3 时停止运行

7.执行上次失败的用例 --last-failed

8.先执行上次失败的用例,再执行成功的用例 --failed-first

9.只收集用例，不执行 --collect-only

10.显示执行最慢的前N条用例：--durations=N -- 示执行最慢的2条用例（所有都会执行，只是最慢的会单独列出）

11.并行执行: -n 2 (需安装pytest-xdist)


其它常用参数

-q: 安静模式, 不输出环境信息

-v: 丰富信息模式, 输出更详细的用例执行信息

-s: 显示程序中的print/logging输出

12.pytest --resultlog=./log.txt 生成log

13.pytest --junitxml=./log.xml 生成xml报告\



python命名规则
一 包名、模块名、局部变量名、函数名
  全小写+下划线式驼峰
  example： this_is_var
二 全局变量
  全大写+下划线式驼峰
  example: GLOBAL_VAR
三 类名
  首字母大写式驼峰，否则会报错提示语法错误
  example: ClassName()

测试用例规则
- 测试文件以test_开头（以_test结尾也行）
- 测试类以Test开头，并且不能带有__init__方法
- 测试函数以test_开头
- 断言使用基本的assert即可
'''

