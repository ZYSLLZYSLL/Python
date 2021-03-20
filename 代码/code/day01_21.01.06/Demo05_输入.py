#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/6 17:06
# @Author : ZY
# @File : Demo05_输入.py
# @Project : code

# input("提示语") 输入的任何数据都是字符串格式的
# 当程序执行到input，等待用户输入，输入完成之后才继续向下执行
# 在python中，input接受用户输入后，一般存储到变量，方便使用
# 在python中，input会把接受到的任意用户输入的数据都当做字符串处理


# 需求：让用户输入姓名和年龄
name = input("请输入您的名字：")
age = input("请输入您的年龄：")
print(f"{name}您的年龄为{age}")
# print(age+2) 是错误的，因为input接收的是str  无法与int运算

