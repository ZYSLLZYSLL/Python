#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/6 16:14
# @Author : ZY
# @File : Demo04_输出_格式化.py
# @Project : code

# print("内容") 将“内容”打印到屏幕上，默认换行

print("hello world")

a = 1
print(a)

# ************ 格式化输出 *************

# %s 字符串
b = "周"
print("****%s*****" % b)
print("****%s%s*****" % (b, "宇"))

# %d 整数
c = 123
print("****%d***" % c)

# %f 浮点数   -- %.2f保留小数点后两位(数字可以改变)
d = 123.1
print("****%f***" % d)
print("****%.2f***" % d)

print("*" * 100)

# format格式化  {}占位符
x = 100
a = "周宇"
print("*****{}*****".format(x))
print("*****{:.2f}*****".format(x))
print("*****{}{}*****".format(x, a))
print("*****{1}{0}*****".format(x, a))
print("*****{} {}*****".format(x, a))

c = 123
print("****%05d***" % c)  # 表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出，宽度为5

# f"{}"格式化 format进阶
print(f"*****{x}*******")
print(f"*****{x:05d}*******")
print(f"*****{x:05d}{0}*******")

# \n 换行符
# \t 制表符（4个空格）
print("*****\n*******")
print("*****\t*******")
print(123, end=",")
print(123, end="\t")
print(123, end="\n")
