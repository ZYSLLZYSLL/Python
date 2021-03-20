#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 10:36
# @Author : ZY
# @File : Demo01_模块和包.py
# @Project : code

"""
    模块分类
        1，系统自带的模块
            os sys time random abc
        2，第三方模块
            pymysql(连接数据库)  paramiko(连接linux)  openpyxl(操作excel)
        3. 自定义的模块

    命名:包的命令，模块的命名
        1，遵守标识符命名规范
        2，不能命名成系统自带的模块名
"""

# 模块的导入

# import sys
# print(sys.path)  # 模块加载的路径

# import pymysql  # 导入第三方模块需要安装

# # 导入本地模块
# import day13.Demo03
# print(day13.Demo03.name)
# day13.Demo03.hanShu()


# from day13.Demo03 import hanShu, name
# hanShu()
# print(name)


# from day13.Demo03 import *
# hanShu()
# print(name)


# from day13.Demo03 import hanShu as b
# b()


# 只导入一部分
from day13.Demo03 import *
# hanShu()
print(name)

# import openpyxl











