#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/19 16:06
# @Author : ZY
# @File : Demo03_正则表达式.py
# @Project : code

"""
. 匹配任意一个字符
* 匹配前一个字符0次或多次
+ 匹配前一个字符1次或多次
? 匹配前一个字符0次或1次
[]匹配括号内任意一个字符
[^]匹配括号外任意一个字符
() 看成一个整体
\b 边界符
{n,m} 匹配前一个字符最少n次最多m次
A|B   匹配A或者B
^
$
"""

import re  # 正则表达式模块

a = """habcdefg
hello
hworld"""
# def findall(pattern（正则表达式）, string（要匹配的字符串）, flags=0（有特殊功能的标志位）):
# c = re.findall('he.*', a)  # ['hello']  因为没有加re.S所以匹配不到特殊字符（换行符\n）
# print(c)

# 取括号里面的值
# c = re.findall('a(.*)de(.*)g', a)  # [('bc', 'f')]
# print(c)

# re.S 给.加功能
# 正则表达式匹配是 贪婪匹配 尽可能匹配多的功能
c = re.findall('h(.*)h', a, re.S)  # ['abcdefg\nhello\n']
print(c)

# 非贪婪模式 在正则表达式符号后面加上 ?
c = re.findall('h(.*?)h', a, re.S)  # ['abcdefg\n']
print(c)
