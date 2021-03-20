#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 11:35
# @Author : ZY
# @File : Demo03_私有权限.py
# @Project : code


# class A():
#     def __init__(self):
#         self.__name = 1
#
#     # def __a(self):
#     def a(self):
#         print(self.__name)
#
#
# # 给属性或者方法加私有权限，属性在外部不可更改，方法在外部不可调用
# a = A()
# a.name = 333  # 更改不了
# a.a()
"""
    修改私有属性
    获取私有属性
"""

class A():
    def __init__(self):
        self.__name = 1

    # def __a(self):
    def a(self):
        print(self.__name)

    # 获取属性值
    def getname(self):
        return self.__name

    # 修改属性值
    def setname(self, name):
        self.__name = name
        return self.__name


# 给属性或者方法加私有权限，属性在外部不可更改，方法在外部不可调用
a = A()
print(a.getname())
print(a.setname('周宇'))

