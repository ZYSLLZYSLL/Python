# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/26 9:41
# @Author : fanfan
# @File : Demo01_stu.py
# @Project : b_2011_code
'''
    添加学员（列表，字典，集合）
	删除学员
	修改学员信息
	查询学员信息
	显示所有学员信息
	退出系统
'''
STU_LIST = []


# 1.显示功能界面
def printInfo():
    print("=" * 40)
    print("1.添加学员".ljust(37, "*"))
    print("2.删除学员".ljust(37, "*"))
    print("3.修改学员信息".ljust(36, "*"))
    print("4.查询学员信息".ljust(36, "*"))
    print("5.显示所有学员信息".ljust(34, "*"))
    print("6.退出系统".ljust(37, "*"))
    print("=" * 40)


# 添加一个学员
def addOneStu(num, name, tel):
    l = []
    l.append(num)
    l.append(name)
    l.append(tel)
    STU_LIST.append(l)


# 删除一个学员
def delOneStu(num):
    # IndexError: list assignment index out of range
    # if len(STU_LIST) == 0:
    #     print("列表中没数据")
    # elif num<len(STU_LIST):
    #     del STU_LIST[num-1]
    try:
        STU_LIST[num - 1] = None
    except IndexError:
        print("数字输入超出列表范围")


# 修改学员信息  num,name,tel
def changeOneStu(num):
    a = int(input('''        1. num
        2. name
        3. tel 请输入你要修改的字段号：'''))
    value = input("请输入你要修改的内容：")
    if 0 < a < 4:
        try:
            STU_LIST[num - 1][a - 1] = value
        except IndexError:
            print("数字输入超出列表范围")


# 查询学员信息
def searchStuInfo(name):
    '''
    :param name: 传入的是姓名或学号
    :return:
    '''
    a = 0
    for i in STU_LIST:  # [[1,'laoli'],[2,'laowang'],[]]
        if name in i:
            a += 1
            print(i)
    if a == 0:
        print("查无此人")


# 显示所有学员信息
def printAllStuInfo():
    print(STU_LIST)


# 退出系统
def exit():
    print("退出系统")


# main方法
def main():
    # 显示功能界面
    printInfo()
    # 输入功能序号
    num = int(input("请输入功能序号："))
    # 根据输入的功能序号实现不同的功能
    if num == 1:
        n = input("请输入学号：")
        name = input("请输入姓名：")
        tel = input("请输入电话号：")
        addOneStu(n, name, tel)
    elif num == 2:
        n = int(input("请输入你要删除的学号："))
        delOneStu(n)
    elif num == 3:
        n = int(input("请输入你要修改的学号："))
        changeOneStu(n)
    elif num == 4:
        n = input("请输入你要查询的学号或姓名：")
        searchStuInfo(n)
    elif num == 5:
        printAllStuInfo()
    elif num == 6:
        exit()


while True:
    try:
        main()
    except:
        print("请重新输入")
