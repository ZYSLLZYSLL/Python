#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 15:35
# @Author : ZY
# @File : Demo05_多态.py
# @Project : code


"""
    多态,一种事务多种形态
"""
# 动物类
class Animal():
    # 公共方法
    def say(self):
        pass


# 狗
class Dog(Animal):
    def say(self):
        print("汪汪")


# 猫
class Cat(Animal):
    def say(self):
        print("喵喵")


# 人
class PeoPle(Animal):
    def say(self):
        print("hello!!!")


# 定义统一的方法
def main(obj):
    obj.say()


p = PeoPle()
m = Cat()
main(m)
