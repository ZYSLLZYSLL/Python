#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/21 16:22
# @Author : ZY
# @File : basePage.py
# @Project : jie_ko
import logging
import time


def systemTime():
    # 时间戳中不能有冒号
    t = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()).split("-")
    t2 = t[2].split(" ")
    s = f"{t[0]}年{t[1]}月{t2[0]}日{t2[1]}时{t[3]}分{t[4]}秒"
    logname = f"{t[0]}年{t[1]}月{t2[0]}日"
    return logname

def jiami(x):
    return "20" + oct(int(str(x)[2:]) * 1000)[2:]

class LogHandler:
    """
        日志，输出到文件，输出到控制台
    """
    # 日志存放路径
    filenamePath = f"../output/log/{systemTime()}.log"
    # 创建一个logging对象，收集日志
    logger = logging.getLogger(__name__)
    # 设置日志等级
    logger.setLevel(level=logging.INFO)
    # 设置文件处理器
    __fhandler = logging.FileHandler(filename=filenamePath, encoding='utf-8')
    # 设置控制台处理器
    __shander = logging.StreamHandler()
    # 设置格式化
    # __format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    __format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # 设置文件处理格式化
    __fhandler.setFormatter(__format)
    # 设置控制台处理格式化
    __shander.setFormatter(__format)
    # 添加处理器
    logger.addHandler(__fhandler)
    logger.addHandler(__shander)
