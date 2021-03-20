#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 15:02
# @Author : ZY
# @File : Demo06_匿名函数.py
# @Project : code

# lambda 匿名函数  只有一个结果时可以使用

def h(a, b):
    return a + b


h(1, 2)

#  这条注释上下两段代码块的效果是一样的

print((lambda a, b: a + b)(1, 2))

# ***********************************

bb = lambda a, b: a + b
print(bb(1, 2))

print((lambda a, b, c='a': 1 if a > 0 else 2)(1, 2))


def h(a, b, *args, c="a", **kwargs):
    return (a, b, c, args, kwargs)


print(h(1, 2, 3, 4, 5, 5, 7, cc=1, vv=2))

# bb = lambda a,b,c="a":a+b
bb = lambda a, b, *args, c="a", **kwargs: (a, b, c, args, kwargs)
print(bb(1, 2, 3, 4, 5, 5, 7, cc=1, vv=2))
