#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 17:30
# @Author : ZY
# @File : Demo02_字符串题.py
# @Project : code

"""
    输入字符串，判断以a开头，b结尾--→输出正确
    以a开头输出以a开头
    以b结尾输出b结尾
    否则输出不正确
"""
a = input("请输入字符串:")
if a.startswith('a') and a.endswith('b'):
    print('正确')
elif a.startswith('a'):
    print('以a开头')
elif a.endswith('b'):
    print('以b结尾')
else:
    print('不正确')
