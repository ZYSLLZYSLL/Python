#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 16:02
# @Author : ZY
# @File : Demo06_类属性和类方法.py
# @Project : code

"""
类属性
"""
# class A():
#     # 类属性
#     name = 'A'
#
#     # 成员属性
#     def __init__(self):
#         self.age = 23
#
#     def printInfo(self):
#         print(A.name)
#
#
# a = A()
# print(a.age)
# a.name = '周宇'
# print(a.name)
# A.name = '博文'
# print(A.name)
#
# b = A()
# print(b.age)
# # b.name = '周宇'
# print(b.name)
# # A.name = '博文'
# print(A.name)
# b.printInfo()

"""
类方法
"""
class A():
    # 类属性
    name = 'A'

    # 成员属性
    def __init__(self):
        self.age = 23

    def printInfo(self):
        print(A.name)

    # 类方法
    @classmethod
    def a(cls):
        print(cls.name)
        print('类方法')


a = A()
a.a()
A.a()

b = A()
b.a()

