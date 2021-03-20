# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/26 14:56
# @Author : fanfan
# @File : main.py
# @Project : b_2011_code

from day18.managerSystem import *
from day18.stu import *

# 创建一个学生管理系统类创建一个学生管理系统的对象
ms = MS()


# main方法
def main():
    # 显示功能界面
    ms.printInfo()
    # 输入功能序号
    num = int(input("请输入功能序号："))
    # 根据输入的功能序号实现不同的功能
    if num == 1:
        n = input("请输入学号：")
        name = input("请输入姓名：")
        tel = input("请输入电话号：")
        # 根据学生类创建了一个学生对象
        s = Stu(n, name, tel)
        ms.addOneStu(s)
    elif num == 2:
        n = int(input("请输入你要删除的学号："))
        ms.delOneStu(n)
    elif num == 3:
        n = int(input("请输入你要修改的学号："))
        ms.changeOneStu(n)
    elif num == 4:
        n = input("请输入你要查询的学号或姓名：")
        ms.searchStuInfo(n)
    elif num == 5:
        ms.printAllStuInfo()
    elif num == 6:
        ms.exit()


while True:
   try:
       main()
   except:
       print("请重新输入")

# import csv
#
# s = Stu('1', 'laoli', '2134124234')
# s1 = Stu('2', 'laowang', '234234324234')
# headers = ['xueHao', 'name', 'age']
# values = [
#     (s.xueHao, s.name, s.tel),
#     (s1.xueHao, s1.name, s1.tel)
# ]
# with open("test.csv", 'w', newline="") as f:
#     # 创建写入对象
#     writer = csv.writer(f)
#     # 写入一行
#     writer.writerow(headers)
#     # 写入多行
#     writer.writerows(values)
# l = []
# with open('test.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for i in reader:
#         s = Stu(i[0], i[1], i[2])
#         l.append(s)
#
# print(l)
