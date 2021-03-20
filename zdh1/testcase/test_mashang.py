#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 19:09
# @Author : ZY
# @File : test_mashang.py
# @Project : zdh1

import pytest
import time

"""
    setup/teardown
    setup_class/teardown_class
"""

# class TestMashang():
#
#     # 这个在所有用例之前只执行一次
#     def setup_class(self):
#         print('在每个类执行前的初始化的工作，比如：创建日志对象，创建数据库的连接，创建接口的请求对象。')
#
#     # 这个在每个用例之前都 执行一次
#     def setup(self):
#         print('\n在执行测试用例之前执行的代码（初始化）例如：打开浏览器，加载网页')
#
#     def test_01_baili(self):
#         print('\n测试百里')
#
#     def test_02_bw(self):
#         print('\n测试博文')
#
#     def teardown(self):
#         print('\n在执行测试用例之后执行的代码（扫尾）例如：关闭浏览器')
#
#     def teardown_class(self):
#         print('在每个类执行后的扫尾的工作，比如：销毁日志对象，断开数据库的连接，断开接口的请求对象。')




class TestMashang:

    def test_01_baili(self,aaa):
        print('\n测试百里')
        print('------'+str(aaa))

    def test_02_bw(self):
        print('\n测试博文')
