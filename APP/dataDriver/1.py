#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 10:03
# @Author : ZY
# @File : 1.py
# @Project : APP
from dataDriver.excelData import ReadExcel, WriteExcel

a = [[1, 2], ["王"]]
WriteExcel("a.xlsx", "博文", "a").set_all_rows(a)

# ReadExcel("a.xlsx").get_all_rows("Sheet1", 0)
