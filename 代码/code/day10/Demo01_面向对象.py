#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 9:14
# @Author : ZY
# @File : Demo01_面向对象.py
# @Project : code
"""
    面向过程：一步一步的去执行代码
        特点：
            1，可扩展性不好
            2，相对面向对象执行效率高
    面向对象：将代码分类封装
        特点：
            1，可扩展性好
            2，执行效率相对面向过程慢一点
    类名是大驼峰命名法
"""


class Test():  # 定义类
    # 成员方法self  作用：代表对象本身，可以在类里面互相使用
    def wash(self):  # 定义成员
        print(f'{self.name}洗衣服')

    def ShuaiGan(self):
        print(f'{self.name}甩干')

    def setAttr(self, name='无名'):
        # 在内部设置 成员属性
        self.name = name


# 定义对象 一个类可以创建多个对象
# Test() 匿名对象，当只需要一个对象的时候可以用
t = Test()
t.setAttr('博文')
# 在外部定义属性
# t.name = 't'
t.wash()
t.ShuaiGan()

print()

f = Test()
f.setAttr('测试')
# f.name = 'f'
f.wash()
f.ShuaiGan()

# 创建类
# class Demo_01():  # 手机
#     def one(self):  # self  对象  内部对象
#         print('hello world')
#         self.two()
#         # self.one()
#
#     def two(self):
#         print('bowen')
#
#
# # 对象    外部对象    类的实例（类的实际例子）
# iphone12 = Demo_01()
# # iphone11 = Demo_01()
# iphone12.one()
# # iphone11.two()

# class Demo_02():
#     def gongNeng(self):
#         print('这个类支持的方法有:\n打印\n复制\n剪切\n备份\n......')
#
#     def xunaZe(self):
#         print('选择你要选择的')
