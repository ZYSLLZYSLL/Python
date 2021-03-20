#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/20 16:34
# @Author : ZY
# @File : Demo24_txt内容到MySQL.py
# @Project : code

import pymysql

f = open('t_to_mysql.txt', 'r', encoding='utf-8')
fr = f.readlines()  # fr是列表
f.close()
# print(fr)
# print(len(fr.split('\n')))

root = pymysql.connect(host='192.168.2.118', user='root', password='123456')
cursor = root.cursor()

cursor.execute('create database if not exists ttomysql;')  # 建库
cursor.execute('use ttomysql')
cursor.execute('create table if not exists web (`名字` char(100), `链接` char(200));')
for i in fr:  # 有几条信息循环多少次，遍历出来的是列表fr里面的字符串内容
    # print(i)
    i = i.split('\t')
    cursor.execute(f"insert into web values ('{i[0]}','{i[1]}')")

# a = cursor.fetchall()
# print(a)

root.commit()
root.close()
