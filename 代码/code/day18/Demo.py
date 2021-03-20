#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/27 15:07
# @Author : ZY
# @File : Demo.py
# @Project : code

# import paramiko
# ssh1 = paramiko.SSHClient()
# ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh1.connect(hostname='192.168.1.111',port=22,username='root',password='111111')
# a,b,c = ssh1.exec_command('ifconfig')
# print(b.read().decode())
# ssh1.close()

# import paramiko
#
# ssh1 = paramiko.Transport(('192.168.1.111', 22))
# ssh1.connect(username='root',password='111111')
# sftp=paramiko.SFTPClient.from_transport(ssh1)
# sftp.get()
# sftp.put()
# ssh1.close()

import os
# a = os.popen('ipconfig')
# print(a.read())
print(os.getcwd())
# os.chdir(r'c:')
print(os.getcwd())
print(os.listdir())
print(os.path.split(r'E:\新\软件测试\5.第五阶段\代码\code\eg\统计cc下每个文件夹各有多少文件 _递归\1.py'))
print(os.path.splitext(r'E:\新\软件测试\5.第五阶段\代码\code\eg\统计cc下每个文件夹各有多少文件 _递归\1.py'))
print(os.path.splitdrive(r'E:\新\软件测试\5.第五阶段\代码\code\eg\统计cc下每个文件夹各有多少文件 _递归\1.py'))


print(os.path.isdir(r'c:'))
print(os.path.isfile('Demo.py'))


