#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 9:52
# @Author : ZY
# @File : Demo01_字符串_判断.py
# @Project : code

# startswith() 判断字符串是否以一个字串或者字符开头，返回True 或者 False
# a = 'ma wElcOme my hoMe'
# print(a.startswith('m'))
# if a.startswith('m'):
#     print('成立')

# endswith() 判断字符串是否以一个字串或者字符结尾，返回True 或者 False
# a = 'ma wElcOme my hoMe'
# print(a.endswith('Me'))
# if a.endswith('Me'):
#     print('成立')

# isalpha() 判断字符串是不是全字母 全是字母返回True 否者 False (有空格也返回False)
# a = 'mawElcOmemyhoMe'
# print(a.isalpha())
# a = 'ma wElcOme my hoMe 1'
# print(a.isalpha())

# isdigit() 判断字符串是不是全是数字
# a = '123456'
# print(a.isdigit())

# isalnum() 字符串全是字母和数字的(全是数字/字母也返回True)
# a = '1234mawElcOmemyhoMe'
# print(a.isalnum())
# a = 'mawElcOmemyhoMe'
# print(a.isalnum())

# isspace() 判断是不是全是空格
# a = '           '
# print(a.isspace())
# a = ''
# print(a.isspace())

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
    print('b结尾')
else:
    print('不正确')





