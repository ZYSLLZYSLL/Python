#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 9:24
# @Author : ZY
# @File : Demo02_传输文件.py
# @Project : code

import paramiko

# 建立传输通道，填入ip地址和端口号，需要是一个元组
a = paramiko.Transport(('192.168.10.24', 22))

# 连接主机
a.connect(username='root', password='111111')

# 创建一个sftp客户端
client = paramiko.SFTPClient.from_transport(a)

# get,从Linux传文件到Windows  get(远程地址， 本地路径)
# client.get('index.html','index.html')

# put,从Windows传文件到Linux  put(本地路径, 远程地址)
client.put('index.html', 'a.html')
client.close()
