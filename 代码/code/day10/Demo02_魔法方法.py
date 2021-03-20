#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 15:19
# @Author : ZY
# @File : Demo02_魔法方法.py
# @Project : code

# # 定义一个洗衣机类
# class Washer():
#     # 定义一个洗衣服的成员方法
#     def wash(self):
#         print(f'{self.name}洗衣服')
#
#     # 定义一个设置属性的成员方法
#     def setAttr(self, name='无名'):
#         # 设置name属性
#         self.name = name
#
#
# haier = Washer()
# haier.setAttr('福桥')
# haier.wash()

# 定义一个洗衣机类
class Washer():
    def __init__(self, name):
        self.name = name
    # 定义一个洗衣服的成员方法
    def wash(self):
        print(f'{self.name}洗衣服')

    # 为了更好看
    def __str__(self):
        return f'用户的名字是:{self.name}'

    # 删除对象默认被调用
    def __del__(self):
        print('删除了该对象')


haier = Washer('博文')
print(haier)
haier.wash()
# 在程序运行中被删除
# del haier

