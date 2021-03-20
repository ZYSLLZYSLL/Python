#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 19:48
# @Author : ZY
# @File : Demo07_while...else.py
# @Project : code


# i = 0
# while i < 5:
#     i += 1
#     print("hello world")
# else:
#     print("输出五次了")

# while不正常结束时，else里的内容不执行
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print("hello world")
else:
    print("输出五次了")

print("*"*20)

# while正常结束时，else里的内容执行
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("hello world")
else:
    print("输出五次了")



