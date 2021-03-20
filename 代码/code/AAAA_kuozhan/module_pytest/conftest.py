#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/5 11:35
# @Author : ZY
# @File : conftest.py
# @Project : code
import pytest

# 自动运行，固定格式，固定文件名 一般放前置后置的文件
# @pytest.mark.usefixtures('init_function')
# print('这里')

"""
    @pytest.fixture(scope="", params="", autouse="", ids="", name="")
    1，scope 表示的是被@pytest.fixture标记的方法的作用域。
    参数：function(默认)（函数），class（类），module（模块），package/session（包）
    2，params：参数化（数据格式，支持列表[]，元组()，字典列表[{},{},{}]，字典元组({},{},{})）
    3，autouse=True：自动执行，默认是False
    4，ids：当使用params参数化时，给每一个值设置一个变量名，意义不大
    5，name：给表示的是被@pytest.fixture标记的方法取一个别名、
    注意：改完名字之和，原本的名字就不能用了，
"""


@pytest.fixture(scope="class")
def init_class():
    # 前置
    print('这是类前置')
    yield
    # 后置
    print('这是类后置')


@pytest.fixture()  # 默认函数级
def init_function():
    # 前置
    print('这是函数前置')
    yield
    # 后置
    print('这是函数后置')


@pytest.fixture(scope="session")
def init():
    # 前置
    print('这是会话列表前置')
    yield
    # 后置
    print('这是会话列表后置')


@pytest.fixture(scope="module")
def init_module():
    # 前置
    print('这是类前置')
    yield
    # 后置
    print('这是类后置')


@pytest.fixture(scope="package")
def init_packages():
    # 前置
    print('这是包前置')
    yield
    # 后置
    print('这是包后置')
