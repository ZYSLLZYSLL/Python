#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 9:35
# @Author : ZY
# @File : 实时查看(每次10秒)内存信息，并保存到txt文件，面向对象.py
# @Project : code

# 实时查看(每次10秒)linux内存信息，并保存到txt文件，面向对象

import paramiko
import time


class CPU():
    def __init__(self, name):
        self.name = name

    def run(self):
        """
        主函数
        :return:
        """
        while True:
            # a = time.time()
            # if int(time.time())+10 == int(time.time()):  # 用于定时
            # 存入当前时间
            self.txt('时间：'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            self.ssh()  # 调用ssh
            print('完成')
            time.sleep(10)  # 系统休眠10秒，用于定时
            # f.write(time.strptime("2021-01-19 15:12:44", "%Y-%m-%d %H:%M:%S"))


    def ssh(self):
        """
        远程连接，用于获取内存信息
        :return:
        """
        client = paramiko.SSHClient()  # 创建连接
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 跳过验证
        # 连接服务器
        client.connect(hostname='192.168.10.24', port=22, username='root', password='111111')
        # 执行获取内存状态的信息
        a, b, c = client.exec_command('free')

        # self.data = b.read().decode()
        self.txt(b.read().decode())  # 调用txt,把内存状态写入文件
        # print(self.deta)

        # print(b.read().decode())
        client.close()  # 断开连接

    def txt(self, data):
        """
        本函数用于写入txt
        :param data:
        :return:
        """
        self.data = data
        f = open(f'{self.name}', 'a', encoding='utf-8')
        f.write(f'{self.data}\n')
        f.close()

a = CPU('a.txt')
a.run()
