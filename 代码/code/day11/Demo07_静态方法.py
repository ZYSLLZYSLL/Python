#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 16:25
# @Author : ZY
# @File : Demo07_静态方法.py
# @Project : code

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

    # 静态方法
    @staticmethod
    def b():
        print('静态方法')


a = A()
a.b()
A.b()

b = A()
b.b()
