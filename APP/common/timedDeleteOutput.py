#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 19:27
# @Author : ZY
# @File : timedDeleteOutput.py
# @Project : APP
import os
import time
from common.allPathSet import AllPathSet

"""
    每三天清除一次output文件里面的内容
"""
class TimedDeleteOutput:
    t = time.time()

    def writeTime(self):
        """
        把时间写入文件
        :return:
        """
        with open("../common/t.txt", "w", encoding='utf-8') as f:
            f.write(str(self.t))

    def removeMkdir(self, filename):
        """
        执行删除和创建文件夹来达成清空文件夹的目的
        :param filename: 要清空的文件夹名字
        :return:
        """
        time.sleep(0.01)
        os.popen(f'rd /s/q {AllPathSet.REMOVE_MKDIR}\{filename}')
        time.sleep(0.01)
        os.popen(f'mkdir {AllPathSet.REMOVE_MKDIR}\{filename}')

    def run(self):
        """
        判断时间是否超过三天，超过就清空文件夹
        :return:
        """
        if os.path.exists("../common/t.txt"):
            with open("../common/t.txt", "r", encoding='utf-8') as f:
                current = float(f.read())
                # print(float(self.t) - current)
                if float(self.t) - current > (3 * 86400):
                    self.removeMkdir("images")
                    self.removeMkdir("log")
                    self.removeMkdir("report")
                    self.removeMkdir("temp")
                    self.writeTime()
        else:
            self.writeTime()
