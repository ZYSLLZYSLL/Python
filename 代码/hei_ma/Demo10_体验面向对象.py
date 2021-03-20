#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/14 10:31
# @Author : ZY
# @File : Demo10_体验面向对象.py
# @Project : code

# 需求：洗衣机。 功能：能洗衣服
# 1，定义洗衣机类
"""
class 类名():
    代码
"""

class XiYiJi():
    def xiYi(self):
        print('我能洗衣服')

# 2，创建对象
# 对象名 = 类名()
haier = XiYiJi()

# 3，验证
# 1，打印haier对象（这是打印出地址）
print(haier)

# 2，使用xiYi功能--> 称为 实例方法/对象方法  -->语法：对象名.实例方法()
haier.xiYi()

