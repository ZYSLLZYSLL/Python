#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/20 15:42
# @Author : ZY
# @File : Demoo2_Pymysql.py
# @Project : code

# import pymysql
#
# """
# :param host: 数据库服务器所在主机地址
# :param user: 登录的用户名
# :param password: 登录的密码
# :param database: 切换的数据 可以选填
# :param port: (default: 3306)
# """
# # 1，连接主机并创建连接对象
# conn = pymysql.connect(host='192.168.10.47', user='root', password='123456')
#
# # 2，创建游标  事务的开启
# cusor = conn.cursor()
#
# # 3，执行sql语句
# cusor.execute('create database if not exists tupian;')
# # cusor.execute('create database tupian;')  # if not exists  如果不存在则创建，存在不报错
# cusor.execute('show databases;')
#
# # 获取上一句代码的全部结果
# # a = cusor.fetchall()
# # print(a)
#
# # # 获取上一句代码的其中一个结果
# # a = cusor.fetchone()
# # print(a)
#
# # # 获取上一句代码的指定数量的结果
# # a = cusor.fetchmany(3)
# # print(a)
#
# # 4，提交数据，将游标数据提交到mysql服务器中
# conn.commit()
#
# # 5，断开连接对象
# conn.close()


import pymysql

"""
:param host: 数据库服务器所在主机地址
:param user: 登录的用户名
:param password: 登录的密码
:param database: 切换的数据 可以选填
:param port: (default: 3306)
"""
# 1，连接主机并创建连接对象
conn = pymysql.connect(host='192.168.1.111', user='root', password='123456')

# 2，创建游标  事务的开启
cusor = conn.cursor()

# 3，执行sql语句
cusor.execute('use zy;')
cusor.execute('desc score;')
a = cusor.fetchall()
print(a)
cusor.execute('select * from score;')
# cusor.execute('create database tupian;')  # if not exists  如果不存在则创建，存在不报错
# cusor.execute('show databases;')

# 获取上一句代码的全部结果
a = cusor.fetchall()
print(a)

# # 获取上一句代码的其中一个结果
# a = cusor.fetchone()
# print(a)

# # 获取上一句代码的指定数量的结果
# a = cusor.fetchmany(3)
# print(a)

# 4，提交数据，将游标数据提交到mysql服务器中
conn.commit()

# 5，断开连接对象
conn.close()
