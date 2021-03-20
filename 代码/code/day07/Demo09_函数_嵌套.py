#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 17:04
# @Author : ZY
# @File : Demo09_函数_嵌套.py
# @Project : code

def h():
    print('h')


def f():
    h()
    print('f')


f()
