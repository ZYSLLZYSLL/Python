#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 9:08
# @Author : ZY
# @File : Demo01_面向对象之继承.py.py
# @Project : code
"""
    单继承
"""

# class A(object):
#     def DaYin(self):
#         print('我是父类A')
#
#
# class B(A):
#     def DaYin(self):
#         # 函数名和父类相同 方法重写 执行子类 不执行父类
#         print('我是子类B,我继承了父类A')
#         print('a\nb')
#
#
# bb = B()  # 子类调用父类的方法
# bb.DaYin()


"""
    多层继承
"""


class A(object):
    def DaYin(self):
        print('我是父类A')


class B(A):
    def DaYin(self):
        # 函数名和父类相同 方法重写 执行子类 不执行父类
        print('我是子类B,我继承了父类A')
        print('a\nb')


class C(B, A):
    pass


cc = C()  # 子类调用父类的方法
cc.DaYin()


#
# class P1(object):
#     def foo(self):
#         print('p1-foo')
#
#
# class P2(object):
#     def foo(self):
#         print('p2-foo')
#
#     def bar(self):
#         print('p2-bar')
#
# class P3(object):
#     def foo(self):
#         print('p3-foo')
#
#     def bar(self):
#         print('p3-bar')
#
# class C1(P1, P2):
#     pass
#
#
# class C2(P1, P2):
#     pass
#
# class C3(P3):
#     def bar(self):
#         print('C3-bar')
#
# class D(C1,C2,C3):
#     pass
#
#
# d = D()
# d.foo()  # 输出 p1-foo
# d.bar()  # 输出 c2-bar

"""
# 多层继承  可以有继承关系
# 单个继承
class A():
    pass


class B(A):
    pass


# 多个继承 不能有继承关系
class A():
    pass


class B():
    pass


class C(A, B):
    pass


# 多层继承  可以有继承关系
class A():
    pass


class B(A):
    pass


class C(B):
    pass
"""