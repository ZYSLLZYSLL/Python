#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/22 11:01
# @Author : ZY
# @File : Demo04_发邮件.py
# @Project : code

import yagmail

# user 邮箱账号
# host 写用到的协议，smtp，163邮箱写smtp.163.com， QQ邮箱写smtp.qq.com
# password 是授权码
yag = yagmail.SMTP(user='zhouyu_114@163.com', host='smtp.163.com', password='BGNFQQXSOYSZBAOS')

contents = ['第一行内容', '第二行内容', yagmail.inline(r'E:\新\软件测试\5.第五阶段\代码\code\dey14\aaaa\冉冉升空的热气球图片.jpg')]
# contents = ['第一行内容', '第二行内容','a.txt',yagmail.inline('图片名')]
yag.send('993464082@qq.com', '标题', contents)
# yag.send(['接收者1','接收者2'], '标题', contents)
