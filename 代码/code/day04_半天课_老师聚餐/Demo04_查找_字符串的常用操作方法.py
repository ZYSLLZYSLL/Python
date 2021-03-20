#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/9 17:01
# @Author : ZY
# @File : Demo04_查找_字符串的常用操作方法.py
# @Project : code


# find(’字串‘，开始下标位置，结束下标位置);检测某个字符串是否包含在这个字符串中，如果在返回这个子符串开始的位置下标，否则返回-1.
a = 'abcdef'
print(a.find("c"))

print('-' * 100)
a = 'hello world'
print(a.find("wo"))  # 6 # 找第一个wo这个字符串开始的位置
print(a.find("o"))  # 4 # 找第一个o这个字符开始的位置
print(a.find("o", 5, 7))  # -1 # 从第5个（包含第5个）开始到第7个之间（不包含7）找第一个o这个字符开始的位置

# index(’字串‘，开始位置，结束位置);检测在某个子串中是否包含在这个字符串中，如果在返回整个字串开始的位置下标，否则报异常。
print('-' * 100)
a = 'hello world'
# print(a.index("woq"))  # 找不到，报异常

# rfind();

# count(’统计的字串‘，开始位置，结束位置);返回某个子串在字符串中出现的次数
print('-' * 100)
a = 'hello world'
print(a.count("wo"))  # 1 # 查找wo这个字符串出现几次
print(a.count("o"))  # 2 # 查找o这个字符出现几次
print(a.count("o", 5, 7))  # 0 # 从第5个开始（包含第5个）到第7个之间（不包含7）查找o这个字符出现几次

