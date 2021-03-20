#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/6 16:12
# @Author : ZY
# @File : Demo03_认识数据类型.py
# @Project : code

a = 1
print(type(a))

b = 1.1
print(type(b))

c = True
print(type(c))

d = "12345"
print(type(d))

e = [10, 20, 30]
print(type(e))

f = (10, 20, 30)
print(type(f))

h = {10, 20, 30}
print(type(h))

g = {"name": "TOM", "age": 20}
print(type(g))

# 整数 123 34 5
print(type(123))  # int
# 浮点数 1.23 4.45
print(type(1.23))  # float
# 布尔值 True False
print(type(True))  # bool
# 字符串 "" '' """ '''
print(type("hello"))  # str
# 列表 [内容1,内容2...]
print(type([1, "afsadff", True]))  # list
print([1, "afsadff", True])
# 元组 (内容1,内容2...)
print(type((1, "afsadff", True)))  # tuple
print((1, "afsadff", True))
# 集合 {内容1,内容2...}
print(type({1, "afsadff", True}))  # set
# 字典 {键1:值1,键2:值2..}
print(type({"name": "老王", 1: "老李"}))  # dict
# 空值 None
print(type(None))  # NoneType

"[1,2,3,4]"  # str
{1, 2, 3, "abc"}  # set
""  # str
''  # str
"{1,23,4}"  # str
{"name": 1, "23": 33}  # dict
(12)  # int
print(type((12)))
