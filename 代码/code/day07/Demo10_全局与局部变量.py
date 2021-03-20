#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 17:21
# @Author : ZY
# @File : Demo10_全局与局部变量.py
# @Project : code

"""
    LEGB规则
    L:local 本地 局部变量  类里面 函数里面 只能在局部使用
    E:
    G:global 全局 全局变量 整个文件 可以在这个文件使用
    B:
"""

# a = 2  # 全局变量
#
#
# def a1():
#     a = 1  # 局部变量
#     print(a)
#
#
# a1()
# print(a)









# a = 2  # 全局变量
#
#
# def a1():
#     global a  # 将局部变量a变成全局变量
#     a = 1
#     print(a)
#
#
# a1()
# print(a)
