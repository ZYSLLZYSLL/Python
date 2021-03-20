#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 16:16
# @Author : ZY
# @File : Demo04_烤地瓜_书上代码.py
# @Project : code

class DiGua():

    def __init__(self):
        self.time = 0
        self.state = ""
        self.tiaoLiao = []

    def __str__(self):
        result = f"当前已烤时间：{self.time}\n"
        result += f"当前状态：{self.state}\n"
        b = ""
        if len(self.tiaoLiao) == 0:
            b = "无"
        else:
            b = ','.join(self.tiaoLiao)
        result += f"当前添加调料：{b}\n"
        return result

    def cook(self, time):
        self.time += time
        if 3 > self.time >= 0:
            self.state = "生的"
        elif 5 > self.time >= 3:
            self.state = "半生不熟"
        elif 8 > self.time >= 5:
            self.state = "熟了"
        elif self.time >= 8:
            self.state = "烤糊了"
        else:
            pass

    def addTL(self, *args):
        self.tiaoLiao.extend(args)


d = DiGua()
d.cook(1)
print(d)
d.cook(5)
print(d)
d.addTL("糖")
print(d)
