#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/1 9:24
# @Author : ZY
# @File : app_启动时间.py
# @Project : app_xingneng

"""
    获取软件启动时间 thisTime
"""
import csv
import os
import time


class App:

    def __init__(self):
        self.launchedResult = ''

    # 启动App
    def launchedApp(self):
        self.launchedResult = os.popen('adb shell am start -W -n com.tal.kaoyan/.ui.activity.HomeTabActivity')
        # return launchedResult

    # 关闭App
    def stopApp(self):
        os.popen('adb shell am force-stop com.tal.kaoyan')
        # return close

    # 获取App的thisTime
    def getThisTime(self):
        for i in list(self.launchedResult):
            if "ThisTime" in i:
                thisTime = i[10:-1]
                return thisTime


class ControlTime:

    def __init__(self, count):
        # 创建App对象
        self.app = App()
        self.time = ""  # app启动时间
        self.t = ""  # 当前时间
        self.count = count  # 总共执行的次数
        self.i = 1  # 当前是执行的第几次

    # 单次执行
    def oneTime(self):
        print(f"开始第{self.i}次启动测试")
        self.app.launchedApp()
        self.time = self.app.getThisTime()
        self.getCurrentTime()
        self.saveData()
        self.app.stopApp()
        print(f"结束第{self.i}次启动测试，剩余{self.count - self.i}次\n")
        time.sleep(1)  # 强制休眠1秒
        if self.i == self.count:  # 执行完毕输出
            print(f'测试结束，共执行了{self.count}次测试')

    def run(self):
        while self.i <= self.count:
            self.oneTime()
            self.i += 1

    def getCurrentTime(self):
        self.t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def saveData(self):
        with open("data.csv", 'a', newline="") as f:
            writer = csv.writer(f)
            if self.i == 1:
                writer.writerow(['执行时间', '执行次数', '启动时间'])
            writer.writerow([self.t, f'第{self.i}次', self.time])


if __name__ == '__main__':
    # 下面这两行是先判断有没有这个文件，有就先删除
    if 'data.csv' in os.popen('dir').read():
        os.popen('del data.csv')
    ControlTime(3).run()

