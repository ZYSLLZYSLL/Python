#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/12 16:08
# @Author : ZY
# @File : Demo07_函数.py
# @Project : code

# 函数的命名必须用小驼峰命名法

"""
    需求：用户到ATM机取钱：
        输入密码后显示"选择功能"界面
        查询余额后显示"选择功能"界面
        取2000钱后显示"选择功能"界面
"""


def xuanZe():
    print('选择功能（假如我有上百行）')


# print('输入密码后')
# xuanZe()
# print('查询余额后')
# xuanZe()
# print('取钱后')
# xuanZe()

# print(xuanZe)  # 代码块所在位置
"""
a = xuanZe  
a()
相当于改了个名字，a()和xuanZe()效果一样
"""
a = xuanZe
a()
