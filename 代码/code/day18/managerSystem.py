# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/26 14:55
# @Author : fanfan
# @File : managerSystem.py
# @Project : b_2011_code

class MS():
    def __init__(self):
        self.l = []

    # 1.显示功能界面
    @staticmethod
    def printInfo():
        print("=" * 40)
        print("1.添加学员".ljust(37, "*"))
        print("2.删除学员".ljust(37, "*"))
        print("3.修改学员信息".ljust(36, "*"))
        print("4.查询学员信息".ljust(36, "*"))
        print("5.显示所有学员信息".ljust(34, "*"))
        print("6.退出系统".ljust(37, "*"))
        print("=" * 40)

    def addOneStu(self,stu):
        '''
        添加学生信息
        :return:
        '''
        self.l.append(stu)

    def delOneStu(self,num):
        '''
        删除学生信息
        :return:
        '''
        try:
            self.l[num-1].xueHao = None
            self.l[num-1].name = None
            self.l[num-1].tel = None
        except IndexError:
            print("索引超出范围")

    # 修改学员信息  num,name,tel
    def changeOneStu(self,num):
        a = int(input('''        1. num
            2. name
            3. tel 请输入你要修改的字段号：'''))
        value = input("请输入你要修改的内容：")
        if 0<a<4:
            try:
                if a == 1:
                    self.l[num - 1].xueHao = value
                elif a == 2:
                    self.l[num - 1].name = value
                elif a == 3:
                    self.l[num - 1].tel = value
            except IndexError:
                print("数字输入超出列表范围")

    # 查询学员信息
    def searchStuInfo(self,name):
        '''
        :param name: 传入的是姓名或学号
        :return:
        '''
        a = 0
        for i in self.l:
            if name == i.xueHao:
                a += 1
                print(i)
            elif name == i.name:
                a += 1
                print(i)
        if a == 0:
            print("查无此人")

    # 显示所有学员信息
    def printAllStuInfo(self):
        for i in self.l:
            print(i.xueHao,i.name,i.tel)

    # 退出系统
    @staticmethod
    def exit():
        print("退出系统")
