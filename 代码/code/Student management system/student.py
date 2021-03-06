#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/16 17:08
# @Author : ZY
# @File : student.py
# @Project : code
"""
    学员信息包含：姓名、性别、手机号；
    添加 __str__ 魔法方法，方便查看学员对象信息
"""


class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'
