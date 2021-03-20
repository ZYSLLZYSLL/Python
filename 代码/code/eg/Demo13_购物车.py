#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 21:16
# @Author : ZY
# @File : Demo13_购物车.py
# @Project : code

"""
    需求：
        1，要求用户输入总金额，例如：2000
        2，显示商品列表，让用户根据序号选择商品，加入购物车
        3，购买，如果商品总金额大于总资产，提示账户余额不足，否则购买成功
        4，附加，可充值，某商品移除购物车
"""
a = ''
money = 0
che = []
zong = 0
goods = [
    {'name': '电脑', 'price': 4999},
    {'name': '鼠标', 'price': 99},
    {'name': '键盘', 'price': 199},
    {'name': '无线网卡', 'price': 69},
    {'name': '水杯', 'price': 49},
    {'name': 'usb拓展孔', 'price': 29},
    {'name': '电脑包', 'price': 109},
]


def inIt():
    """本方法是功能显示界面"""
    global a
    print('\n\n')
    print('-*' * 50, '-')
    print(' ' * 35, end='')
    print('---欢迎登万家乐购物系统---\n')
    print(' ' * 40, end='')
    print('1:查询余额')
    print(' ' * 40, end='')
    print('2:充   值')
    print(' ' * 40, end='')
    print('3:加入购物车')
    print(' ' * 40, end='')
    print('4:从购物车删除商品')
    print(' ' * 40, end='')
    print('5:结算')
    print(' ' * 40, end='')
    print('6:退出系统')
    a = input('请输入对应的序号来选择你要操作的功能:')
    print('-')


def xianS(a, b):
    """本函数显示当前购物车商品和价格"""
    global zong
    for k in range(len(a)):
        print(f'{k + 1}\t', end='')
        print(f"{a[k]['name']: <10s}", end='')
        # print(' ' * (11 - len(a[k]['name'])), end='')
        if b:
            zong += int(a[k]['price'])
        print(a[k]['price'])
    if b:
        print(f'当前购物车商品总金额为: {zong} 元')
        zong = 0


def shopping():
    """本方法是购物车 添加 商品的功能"""
    while True:
        global zong
        print('序号', '商品', '        价格')

        xianS(goods, False)

        b = int(input('\n请输入您要加入购物车商品的序号(退出添加请输入‘00’):'))
        print()
        if b == 00:
            break
        elif b > len(goods):
            print('*****  请输入正确的序号  *****\n')
        else:
            che.append(goods[b - 1])
            print('当前购物车内商品为:')
            print('序号', '商品', '        价格')

            # zong = 0
            xianS(che, True)

            print()
            c = input('请问您还要继续添加商品吗？（Y/N）')

            if c == 'N' or c == 'n':
                break


def delete():
    """本方法是购物车 删除 商品的功能"""
    while True:
        global zong
        if len(che) == 0:
            print('当前购物车内是空的哦')
            break
        print('您当前购物车的商品如下:')
        print('序号', '商品', '        价格')

        xianS(che, True)

        b = int(input('\n请输入您要从购物车删除商品的序号(退出删除请输入‘00’):'))
        print()
        if b == 00:
            break
        elif b > len(che):
            print('*****  请输入正确的序号  *****\n')
        else:
            del che[b - 1]
            # che.append(goods[b - 1])
            print('当前购物车内商品为:')
            print('序号', '商品', '        价格')

            xianS(che, True)

            print()
            c = input('请问您还要继续删除商品吗？（Y/N）')

            if c == 'N' or c == 'n':
                break


def Settlement():
    """本函数用于结算购物车"""
    # xianS(che, True)
    global zong
    global money
    for k in range(len(che)):
        print(f'{k + 1}\t', end='')
        print(che[k]['name'], end='')
        print(' ' * (11 - len(che[k]['name'])), end='')
        zong += int(che[k]['price'])
        print(che[k]['price'])

    print(f'当前购物车商品总金额为: {zong} 元\n')
    bb = input(f'当前购物车内商品总金额为 {money} 元，商品如上，是否确认付款？（Y/N）')

    if bb == 'y' or bb == 'Y':
        password = input('请输入六位密码:\n')
        if zong > money:
            print('账户余额不足,请删除一些商品或者充值')
            zong = 0
        else:
            print('\n商品购买成功\n')
            money = money - zong
            print(f'当前余额为 {money} 元')
            che.clear()


while a == '':  # 让输入总资产的语句只执行一次
    print('-*' * 50, '-')
    print(' ' * 35, end='')
    print('---欢迎光临万家乐购物系统---\n')
    money = int(input('请输入总资产:'))
    print(f'您的总资产为 {money} 元')
    while True:
        inIt()
        if a == '1':
            print(f'您的余额为 {money} 元')
        elif a == '2':
            b = int(input(f'当前余额为 {money} 元，请输入您要充值的金额:'))
            money += b
            print(f'充值成功，您充值了 {b} 元，当前余额为 {money} 元')
        elif a == '3':
            shopping()
        elif a == '4':
            delete()
        elif a == '5':
            Settlement()
        elif a == '6':
            a = input('您确定退出程序吗？（Y/N）')
            if a == 'Y' or a == 'y':
                print('\n************  欢迎下次光临  ************')
                break
