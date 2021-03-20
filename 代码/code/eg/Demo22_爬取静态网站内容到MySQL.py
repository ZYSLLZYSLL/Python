#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/20 16:34
# @Author : ZY
# @File : Demo22_爬取静态网站内容到MySQL.py
# @Project : code

import re
import requests
import pymysql

html = requests.get("https://www.ivsky.com/tupian/jiaotongyunshu/")
a = html.content.decode('utf-8')
c = re.findall("<ul(.*?)</ul>", a)
jpg = re.findall('img src="(.*?)"', c[2])
title = re.findall('alt="(.*?)">', c[2])

root = pymysql.connect(host='192.168.10.47', user='root', password='123456')
cursor = root.cursor()
cursor.execute('create database if not exists tupian;')
cursor.execute('use tupian;')  #
cursor.execute('create table if not exists web (`名字` char(20),`链接` char(200));')
for i in range(len(jpg)):
    # print(title[i],jpg[i])
    cursor.execute(f"insert into web values ('{title[i]}','{jpg[i]}')")
# qq = cursor.fetchall()
# print(qq)
root.commit()
root.close()
