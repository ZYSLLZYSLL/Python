#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 9:14
# @Author : ZY
# @File : Demo02_返回值作为参数传递_多个返回值.py
# @Project : code

# 返回值作为参数传递
# def fanHui():
#     return 4
#
#
# def daYin(a):
#     print(a)
#
#
# daYin(fanHui())

# 返回值作为参数来传递
# 返回值可以返回多个数据(Python的所有数据类型)，以元组    展示
def hanshu():
    return 3, 5454, 1.23, [1, 2, 3]


def num(a):
    print(a)


num(hanshu())
