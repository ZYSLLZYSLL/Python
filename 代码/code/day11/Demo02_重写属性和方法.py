#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 10:43
# @Author : ZY
# @File : Demo02_重写属性和方法.py
# @Project : code


"""
    # 单继承
"""

# class A():
#     def __init__(self):
#         self.name = 1
#
#     def a(self):
#         print(self.name)
#
#
# # 调用父类的属性和方法
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.age = 20  # 也可以添加属性
#
#     def a(self):
#         A.a(self)
#         self.name = '周宇'
#         print(self.name)
#         print('b')
#         print(self.age)
#
#
# B().a()

"""
    多继承
"""

# class C():
#     def __init__(self):
#         self.bowen = 'c'
#
#     def c(self):
#         print(self.bowen)
#
#
# class A():
#     def __init__(self):
#         self.name = 'a'
#
#     def a(self):
#         print(self.name)
#
#
# # 调用父类的属性和方法
# class B(A, C):
#     def __init__(self):
#         A.__init__(self)
#         C.__init__(self)
#         self.age = 'b'  # 也可以添加属性
#
#     def a(self):
#         A.a(self)
#         C.c(self)
#         self.name = '周宇'
#         print(self.name)
#         print(self.age)
#
#
# B().a()

"""
super().a()  # 调用父类的方法
"""


class C():
    def __init__(self):
        self.bowen = 'c'

    def c(self):
        print(self.bowen)


class A():
    def __init__(self):
        self.name = 'a'

    def a(self):
        print(self.name)


# 调用父类的属性和方法
class B(A, C):
    def __init__(self):
        A.__init__(self)
        C.__init__(self)
        self.age = 'b'  # 也可以添加属性

    def a(self):
        super().a()  # 调用父类的方法
        # super(B, self).a()  # 这个和上面的一样效果
        A.a(self)
        C.c(self)
        self.name = '周宇'
        print(self.name)
        print(self.age)


B().a()
