#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 16:39
# @Author : ZY
# @File : test_pytest_01.py
# @Project : Appium
import pytest

"""
    pytest:单元测试框架  灵活，插件多，报告美观
    unittest:单元测试框架
    robot_framework:单元测试框架
"""
"""
    pytest查找规则:文件查找顺序按照ASCII码执行，同一文件是按照从上到下
        测试文件以test_开头或者以_test.py结尾
        测试函数以test开头
        测试方法以test开头
        测试类以Test开头
        所有包必须有__init__.py模块
        测试类不能有__init__方法
"""

"""
参数
    -v:用于显示每个测试函数的执行结果
    -q:只显示整体测试结果
    -s:输出print函数的功能
    -h:帮助
    -x:碰到第一个fail就停止
    -- maxfail:设置最大允许fail数
    -k 根据关键字来匹配执行的用例(关键字不能用数字)
"""


def test_01b():
    print('\n这是test_pytest_01里面的test_01')


def test_02c():
    # assert 1 == 2
    print('\n这是test_pytest_01里面的test_02')


if __name__ == '__main__':
    # 在文件中执行
    # -k 根据关键字来匹配执行的用例(关键字不能用数字)  pytest.main(['-sv', '--maxfail=2'])
    # 节点执行  由模块名，分隔符，类名，分隔符，方法名/函数名组成 pytest test_pytest_01.py::test_01b
    pytest.main(['-sv', '--maxfail=2'])
