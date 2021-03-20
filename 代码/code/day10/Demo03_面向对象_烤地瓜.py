#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/15 15:58
# @Author : ZY
# @File : Demo03_面向对象_烤地瓜.py
# @Project : code

"""
烤地瓜
需求
需求主线：
    1.被烤的时间和对应的地瓜状态：
        0-3分钟：生的
        3-5分钟：半生不熟
        5-8分钟：熟的
        超过8分钟：烤糊了
    2. 添加的调料： ⽤户可以按自己的意愿添加调料
"""


class KaoDiGua():
    def __init__(self, time, liao='不添加'):
        self.time = time
        self.liao = liao
        print(f'客户选择 {self.liao} 调料')

    def di_time(self):
        if 0 <= self.time < 3:
            print(f'刚烤{self.time}分钟，地瓜是生的\n')
        elif 3 <= self.time < 5:
            print(f'刚烤{self.time}分钟，地瓜是半生不熟的\n')
        elif 5 <= self.time < 8:
            print(f'刚烤{self.time}分钟，地瓜熟了\n')
        elif self.time >= 8:
            print(f'烤了{self.time}分钟了，地瓜已经烤糊了\n')


zhou = KaoDiGua(7)
zhou.di_time()

zhou1 = KaoDiGua(7, '辣椒')
zhou.di_time()
