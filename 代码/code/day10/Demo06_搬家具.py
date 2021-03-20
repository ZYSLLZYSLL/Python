#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 17:37
# @Author : ZY
# @File : Demo06_搬家具.py
# @Project : code

# 房子类
class House():

    def __init__(self, addr, area):
        self.addr = addr
        self.area = area
        self.free = self.area
        self.funcList = []

    def __str__(self):
        result = f"当前位置：{self.addr}\n"
        result += f"总面积：{self.area}平方米\n"
        result += f"剩余面积：{self.free}平方米\n"
        b = ""
        if len(self.funcList) == 0:
            b = "无"
        else:
            b = ','.join(self.funcList)
        result += f"当前房子家具列表：{b}\n"
        return result

    def banJiaJu(self, fo):
        c = fo.area
        if c > self.free or c < 0:
            print("剩余面积不够了或输入错误")
        else:
            self.free -= c
            self.funcList.append(fo.name)


# 家具类
class Func():

    def __init__(self, name, area):
        self.name = name
        self.area = area


h = House("北京", 120)
bed = Func("床", 10)
h.banJiaJu(bed)
print(h)
