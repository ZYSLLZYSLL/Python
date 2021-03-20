#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/19 15:01
# @Author : ZY
# @File : Demo02_time.py
# @Project : code

import time

# 时间戳
a = time.time()
print(a)

# 结构化时间   东八区时间（北京时间）
c = time.localtime()
print(c)

# UTC时间，国际时间，和北京时间差八个小时
d = time.gmtime()
print(d)

# 格式化时间  结构转格式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式转结构
print(time.strptime("2021-01-19 15:12:44", "%Y-%m-%d %H:%M:%S"))

# 结构转时间戳
print(time.mktime(time.localtime()))

# 系统强制休眠
# for i in range(10):
#     print(i)
#     time.sleep(2)

# 需求：计算从出生到现在经过了多少秒
# 1，先算出出生时间的时间戳
aa = time.strptime("1998-08-09 00:00:00", "%Y-%m-%d %H:%M:%S")
aa1 = time.strptime("2000-01-14 00:00:00", "%Y-%m-%d %H:%M:%S")
dd = time.mktime(aa)
dd1 = time.mktime(aa1)
# 2，算出当前时间戳
bb = time.time()
# 3，求差
print(f'宝宝出生了 {bb - dd} 秒')
print(f'周宇出生了 {bb - dd1} 秒')
print(f'宝宝比我大了 {(bb - dd)-(bb - dd1)} 秒\n{((bb - dd)-(bb - dd1))/86400} 天\n{(((bb - dd)-(bb - dd1))/86400)/365} 年')

