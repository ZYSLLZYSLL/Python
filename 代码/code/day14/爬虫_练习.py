#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/19 20:36
# @Author : ZY
# @File : 爬虫_练习.py
# @Project : code

import requests  # 爬虫模块，进行网络接口连接
import re
name = 1

html = requests.get('http://www.kfu.edu.cn/xxgk/xyfg.htm')
result = html.content.decode('utf-8')
# print(result)
c = re.findall('<div style="(.*?)</a></div>', result)
d = re.findall('href="..(.*?)">', c[0])
# print(d)

for i in d:
    j = requests.get('http://www.kfu.edu.cn' + i)
    w = j.content.decode('utf-8')
    jj = re.findall('src="/__local(.*?)" ', w)
    print(jj)
    j =requests.get('http://www.kfu.edu.cn/__local' + jj[0])

    # 把爬到的二进制存到文件里
    a = open(f"kd\\{name}.jpg", 'wb')
    name += 1
    a.write(j.content)
    a.close()

# for i in d:
#     j = requests.get('http://www.kfu.edu.cn' + i)
#     w = j.content.decode('utf-8')
#     jj = re.findall('src="/__local(.*?)" ', w)
#     j =requests.get('http://www.kfu.edu.cn/__local' + jj[0])
#     print(jj[0])
#
#     # 把爬到的二进制存到文件里
#     a = open(f"kd\\{name}.jpg", 'wb')
#     name += 1
#     a.write(j.content)
#     a.close()
