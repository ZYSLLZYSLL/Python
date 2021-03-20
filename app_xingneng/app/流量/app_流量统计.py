#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/1 14:03
# @Author : ZY
# @File : app_流量统计.py
# @Project : app_xingneng
import csv
import os
import time


class App:

    def __init__(self):
        self.launchedResult = ''
        self.pid = ''
        self.liuliang = ''

    # 启动App
    def launchedApp(self):
        os.popen('adb shell am start -W -n com.tal.kaoyan/.ui.activity.HomeTabActivity')
        # self.launchedResult = os.popen('adb shell am start -W -n com.tal.kaoyan/.ui.activity.HomeTabActivity')
    # return launchedResult

    # 关闭App
    def stopApp(self):
        os.popen('adb shell am force-stop com.tal.kaoyan')

    # 获取pid
    def getPid(self):
        self.pid = list(os.popen('adb shell ps | find "com.tal.kaoyan"'))[0].split(' ')[4]

    def aaaaa(self):
        pass

    # 获取App的流量
    def getliuliang(self):
        temp = list(os.popen(f'adb shell cat /proc/{self.pid}/net/dev'))[-1].split(' ')
        for i in range(len(temp)):
            if '' in temp:
                temp.remove('')

        receive = temp[1]
        transmit = temp[9]

        return int(receive) + int(transmit)

    # monkey随机操作手机
    def monkey(self):
        os.popen('adb shell monkey -p com.tal.kaoyan --pct-touch 100 --throttle 50 -v -v -v 200')


class ControlTime:

    def __init__(self, count):
        # 创建App对象
        self.app = App()
        self.time = ""  # 启动时间
        self.t = ""  # 当前时间
        self.count = count  # 总共执行的次数
        self.i = 1  # 当前是执行的第几次

    # 单次执行
    def one(self):
        print(f"开始第{self.i}次流量测试")
        self.app.launchedApp()
        time.sleep(2)  # 强制休眠1秒
        self.app.getPid()
        liuliang1 = self.app.getliuliang()
        self.app.monkey()
        liuliang2 = self.app.getliuliang()
        self.app.liuliang = liuliang2 - liuliang1
        self.getCurrentTime()
        self.saveData()
        self.app.stopApp()
        print(f"结束第{self.i}次流量测试，剩余{self.count - self.i}次\n")
        time.sleep(2)  # 强制休眠1秒
        if self.i == self.count:  # 执行完毕输出
            print(f'测试结束，共执行了{self.count}次测试')


    def run(self):
        while self.i <= self.count:
            self.one()
            self.i += 1

    def getCurrentTime(self):
        self.t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def saveData(self):
        with open("data.csv", 'a', newline="") as f:
            writer = csv.writer(f)
            if self.i == 1:
                writer.writerow(['执行时间', '执行次数', '流量'])
            writer.writerow([self.t, f'第{self.i}次', self.app.liuliang])


if __name__ == '__main__':
    # ControlTime(1).one()
    ControlTime(30).run()
    # App().getliuliang()
