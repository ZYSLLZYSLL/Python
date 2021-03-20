#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 9:03
# @Author : ZY
# @File : Demo01_paramiko模块.py
# @Project : code

import paramiko

# 创建远程客户端
client = paramiko.SSHClient()

# 自动跳过主机验证
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 连接服务器，Linux用户名，密码
client.connect(hostname='192.168.10.24', port=22, username='root', password='111111')

# 执行命令
stuin, stuout, stuerr = client.exec_command('pwd;ls')
# stuin, stuout, stuerr = client.exec_command("ls -l | grep '^-' | wc -l")  # 统计本目录下有多少普通文件

"""
    styin:执行的命令
    stuout:执行的结果
    stuerr:执行的错误
"""
print(stuout.read().decode())

# 断开连接
client.close()
