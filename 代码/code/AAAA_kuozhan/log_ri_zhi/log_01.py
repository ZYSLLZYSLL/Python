#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 11:08
# @Author : ZY
# @File : log_01.py
# @Project : Appium

import logging

class Logg:
    # 创建一个logging对象，收集日志
    logger = logging.getLogger(__name__)
    # 设置日志等级
    logger.setLevel(level=logging.DEBUG)
    # FileHandler输出到文件中
    handler = logging.FileHandler("a.txt", encoding='utf-8')
    # StreamHandler输出到控制台
    shandler = logging.StreamHandler()
    # 设置Formatter设置格式
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    # 处理器设置输出格式
    handler.setFormatter(formatter)
    # 控制台处理设置输出格式
    shandler.setFormatter(formatter)
    # 将处理器添加到日志收集器中
    logger.addHandler(handler)
    # 将控制台处理器添加到日志收集器中
    logger.addHandler(shandler)

    def get_info(self, info):
        self.logger.info(info)

    def get_DEBUG(self, debug):
        self.logger.debug(debug)




# logging.StreamHandler()

# level是用来设置收集的等级 encoding
# format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
# logging.basicConfig(filename="my.txt", level=logging.DEBUG, format=format)
#
# logging.debug("这是debug")
# logging.info("这是info")
# logging.warning("这是waring")
# logging.error("这是error")
# logging.critical("这是critical")
#
# # 这是另一种写法
# logging.log_ri_zhi(logging.DEBUG, "这是debug")
