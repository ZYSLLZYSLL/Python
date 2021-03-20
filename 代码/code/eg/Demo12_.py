#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 14:45
# @Author : ZY
# @File : Demo12_.py
# @Project : code

"""
    需求：进入系统显示系统功能页面，功能如下：
        添加学员
        删除学员
        修改学员信息
        查询学员信息
        显示所有学员信息
        退出系统
        系统共6个功能，用户根据自己需求选取。

    步骤分析
    1.显示功能界面
    2.用户输入功能序号
    3.根据用户输入的功能序号，执行不同的功能（函数）
        3.1 定义函数
        3.2 调用函数

"""
change_name = ''  # 修改学员信息时用到的
a = ''  # 命令界面使用
xinXi = []


def inIt():
    global a
    print('\n\n')
    print('*-' * 50, '-')
    print(' ' * 30, end='')
    print('---欢迎登陆博文智生2011届学员管理系统---\n')
    print(' ' * 40, end='')
    print('1:添加学员')
    print(' ' * 40, end='')
    print('2:删除学员')
    print(' ' * 40, end='')
    print('3:修改学员信息')
    print(' ' * 40, end='')
    print('4:查询学员信息')
    print(' ' * 40, end='')
    print('5:显示所有学员信息')
    print(' ' * 40, end='')
    print('6:退出系统')
    a = input('请输入对应的序号来选择你要操作的功能:')
    print('-')


def no1():
    """本函数添加学员的基本信息"""
    add_name = input('请输入姓名:')
    add_gender = input('请输入性别:')
    add_age = input('请输入年龄:')

    global xinXi

    for i in xinXi:
        if add_name == i['name']:
            print(f' {add_name} 学员的信息已经存在，请勿重新添加')
            return

    add_xin_xi = {}

    add_xin_xi['name'] = add_name
    add_xin_xi['gender'] = add_gender
    add_xin_xi['age'] = add_age

    xinXi.append(add_xin_xi)

    print(f'成功添加 {add_name} 学员的信息')
    print(xinXi)


def no2():
    """本函数删除学员的基本信息"""
    del_name = input('请输入你要删除学员的姓名:')

    for j in xinXi:
        if del_name == j['name']:
            print(f"{del_name} 学员信息为:{j}")
            for i in xinXi:
                if del_name == i['name']:
                    xinXi.remove(i)

            print(f'成功删除 {del_name} 学员的信息')
            print(xinXi)
            return
    else:
        print(f"{del_name} 学员不存在，请确认后再删除")


def change():
    global change_name
    change_name = input('请输入你要修改学员的姓名:')
    project = input('请输入你要修改学员的那一部分信息（name，gender，age）:')
    change_value = input('请输入你要修改的新内容:')

    for i in xinXi:
        if change_name == i['name']:
            i[project] = change_value


def no3():
    """本函数修改学员的基本信息"""
    global change_name
    change_name = input('请输入你要修改学员的姓名:')

    for i in xinXi:
        if change_name == i['name']:
            print(f"{change_name} 学员信息为:{i}")
            a = input('您是要修改几个内容呢？（1，2，3）')
            if a == '1':
                change()
            elif a == '2':
                change()
                change()
            elif a == '3':
                print('修改三个信息你不会删除重新添加啊，啥也不是')

            if a != '3':
                print(f'成功修改 {change_name} 学员的信息')
                print(xinXi)
            return
    else:
        print(f"{change_name} 学员不存在，请确认后再修改")


def no4():
    """本函数查询学员的基本信息"""
    Inquire_name = input('请输入你要修改学员的姓名:')

    for i in xinXi:
        if Inquire_name == i['name']:
            print(f"{Inquire_name} 学员信息为:{i}")
            return
    else:
        print(f"{Inquire_name} 学员不存在，请确认后再查询")


def no5():
    """本函数显示所有学员的基本信息"""
    print('name', ' gender', '   age')

    for k in range(len(xinXi)):
        print(xinXi[k]['name'], end='\t\t')
        print(xinXi[k]['gender'], end='\t\t')
        print(xinXi[k]['age'], end='\t\t\n')


def student():
    while True:
        global a
        inIt()
        if a == '1':
            no1()
        elif a == '2':
            no2()
        elif a == '3':
            no3()
        elif a == '4':
            no4()
        elif a == '5':
            no5()
        elif a == '6':
            a = input('您确定退出程序吗？（Y/N）')
            if a == 'Y' or a == 'y':
                break
