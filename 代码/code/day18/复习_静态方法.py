# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 9:33
# @Author : fanfan
# @File : 复习_静态方法.py
# @Project : b_2011_code

class A():
    def __init__(self):
        self.__aaaa = 1  # 私有属性，外部无法调用，只能内部使用
        # get获取属性 set设置属性

    def setAAAA(self, b):  # 设置属性
        self.__aaaa = b

    def getAAAA(self):  # 获取属性
        return self.__aaaa

    # 对象调用的成员方法，类方法，静态方法 传的是self
    def a(self):
        print('a')
        self.aa()
        self.aaa()

    # 类调用的类方法，静态方法  传的是cls  公共的操作
    @classmethod
    def aa(cls):
        # cls.a()  # 缺一个对象
        print("aa")
        cls.aaa()

    # 对象和类都能使用 什么都不用传  省资源
    @staticmethod
    def aaa():
        print("aaa")


print(sum(range(1, 101)))
