#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 9:04
# @Author : ZY
# @File : Demo01_异常.py.py
# @Project : code

"""
    异常: 是可以被开发人员捕获的
        print(a) #
        Traceback (most recent call last):
          File "E:/b_2011_code/day13/Demo01.py", line 12, in <module>
            print(a)
        NameError: name 'a' is not defined

    错误:是不能被捕获的，一般为系统错误
        print(
        File "E:/b_2011_code/day13/Demo01.py", line 29

            ^
        SyntaxError: unexpected EOF while parsing
"""

"""
    1，把可能发生异常的代码捕获到，让我们的程序正常执行
    2，我们本身就想让程序发生异常
"""

# 捕获异常

# try:
#     print(a)
# except:
#     print('出现异常了')


# 捕获指定异常

# try:
#     print(a)
# except NameError:
#     print('出现异常了')


# 捕获指定异常并查看提示信息

# try:
#     print(a)
# except NameError as bb:
#     print('出现异常了', bb)


# 捕获 所有 异常并查看提示信息
# Exception代表所有异常

# try:
#     print(a)
# except Exception as bb:
#     print('出现异常了', bb)


# else,当try里不发生异常，执行else里面的语句

# try:
#     print(a)
# except Exception as bb:
#     print('出现异常了', bb)
# else:
#     print('没有发生异常')


# finally 不管有没有异常我都执行

# try:
#     print(a)
# except Exception as bb:
#     print('出现异常了', bb)
# else:
#     print('没有发生异常')
# finally:
#     print('finally 不管有没有异常我都执行')

# try...except NameError...except TypeError...except ExceptionError

try:
    print(a)
except NameError as bb:
    print(bb)
except TypeError as cc:
    print(cc)
except Exception as dd:
    print(dd)


# 自定义异常
class PasswordErrorpp(Exception):
    def __init__(self, m, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.m = m

    def __str__(self):
        return f'{self.m}'


# 触发异常
raise PasswordErrorpp(121345)
