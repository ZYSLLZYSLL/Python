#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 9:24
# @Author : ZY
# @File : Demo03_函数的参数.py
# @Project : code

"""
    函数的参数：
        1，位置参数（必填参数）
        2，关键字参数（必填参数）
        3，缺省参数（默认参数） 非必填
        4，不定长参数（可变长参数）  非必填
            包裹位置传递
            包裹关键字传递
"""


# 位置参数  所有python类型皆可传入
def daYin(a, b, c, d):  # 这里的a是必填参数，调用时不填写会报错，可以
    print(a, b, c, d)


daYin(1, 2, 3, 0)  # 1 2 3 0

# 关键字参数  直接指明我要把值传给谁
daYin(b=8, a=9, d=7, c=1)  # 9 8 1 7


# 缺省参数 （也叫默认参数）
def a(a=1, b=2):
    print(a, b)


a()  # 当不给参数时，打印默认   1 2
a(4, 5)  # 当给参数时，打印给的数字   4 5


# 不定长参数--包裹 位置 传递
def bb(*args):  # args是python自定义的名字，可以自己修改
    print(args)


bb(1, 2, 3, 42)  # 返回一个元组  (1, 2, 3, 42)


# 不定长参数--包裹 关键字 传递
def bb1(**kwargs):  # kwargs是python自定义的名字，可以自己修改
    print(kwargs)


bb1(a=1, b=2, name='周宇')  # 返回一个字典   {'a': 1, 'b': 2, 'name': '周宇'}

print(('*' * 100))


# ***************************************************************************

def hhh(a, b, *args, c=1, **kwargs):    # a，b不能用关键字参数,同样在kwargs里也不能用a,b
    print(a, b, *args, c, kwargs)


hhh(1, 2, 3, 4, c=10, name=1)
