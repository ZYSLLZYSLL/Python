#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 10:40
# @Author : ZY
# @File : Demo03_条件语句.py
# @Project : code


# 网吧基础

# age = 20
#
# if age >= 18:
#     print("已经成年，可以上网")
#
# print("判断完毕，系统关闭")

"""
    网吧进阶题
    要求：用户自己输入年龄，系统判断，
    若是常年则输出“您的年龄是x，已经成年，可以上网”
"""

# age = input("请输入您的年龄:")
#
# if int(age) >= 18:
#     print(f"您的年龄是{age}岁，已经成年，可以上网")
# else:
#     print(f"您的年龄是{age}岁，未常成年，按照规定不可以上网")


# 烤地瓜，地瓜初始状态生的（0） 半生不熟（1-3） 熟了（4-6） 熟透了（7-8） 焦了（>=9）

a = int(input("请输入数字："))

if a == 0:
    print("地瓜是生的")
elif 1 <= a <= 3:
    print("地瓜是半生不熟")
elif 4 <= a <= 6:
    print("地瓜是熟的，可以吃了")
elif a == 7 or a == 8:
    print("地瓜已经熟透了，再不吃就焦了")
elif a >= 9:
    print("地瓜已经焦了")
else:
    print("你的地瓜是还没种出来吗？")

"""
坐公交：如果有钱可以上车，没钱不能上车；
上车后如果有空座，则可以坐下；如果没空座，就要站着。怎么书写程序？
"""

print("注意，公交车来了")
money = input("请问你有钱吗？(Y/N):")
if money == "Y":
    print("请上车")

    seat = input("您已经上车了，您看一下还有座位吗？（Y/N）:")

    if seat == "Y":
        print("好的，请坐")
    else:
        print("对不起，没有座位了，您就站一会吧")
elif money == "N":
    print("对不起，没有钱是不能上车的")


