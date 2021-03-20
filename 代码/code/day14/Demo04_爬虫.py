#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/19 16:29
# @Author : ZY
# @File : Demo04_爬虫.py
# @Project : code

# import requests
# import re
# r"""Sends a GET request.
#
#    :param url: url地址
#    :param params: (optional) Dictionary, ?键=值  {键：值}
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object  响应对象
#    :rtype: requests.Response
#    """
# html = requests.get("https://www.ivsky.com/tupian/jiaotongyunshu/")
# # content是以二进制的方式展示  encode 编码 decode 解码
# result = html.content.decode("utf-8")
# c = re.findall("<ul(.*?)</ul>",result)  # ['ul','ul','ul']
# # print(c[2])
# jpg= re.findall('img src="(.*?)"',c[2])
# title = re.findall('alt="(.*?)">',c[2])
# print(jpg)
# print(title)
# # 获取图片
# j = requests.get("https:"+"//img.ivsky.com/img/tupian/li/202006/25/shatanche-008.jpg")
# # print(j.content)
#
# a = open("a.jpg",'wb')
# a.write(j.content)
# a.close()


import requests  # 爬虫模块，进行网络接口连接
import re

r"""Sends a GET request.

   :param url: url地址   
   :param params: (optional) Dictionary, ?键=值  {键：值}
   :param \*\*kwargs: Optional arguments that ``request`` takes.
   :return: :class:`Response <Response>` object  响应对象
   :rtype: requests.Response
   """
html = requests.get("https://www.ivsky.com/tupian/jiaotongyunshu/")
# content是以二进制的方式展示  encode 编码 decode 解码
result = html.content.decode("utf-8")  # 解码出来是网页源代码
c = re.findall("<ul(.*?)</ul>", result)  # ['ul','ul','ul']
# print(c[2])
jpg = re.findall('img src="(.*?)"', c[2])
title = re.findall('alt="(.*?)">', c[2])
# print(jpg)
# print(title)
# 获取图片

for i in jpg:
    j = requests.get("https:" + i)
    # print(j.content)

    # 把爬到的二进制存到文件里
    a = open(f"aaaa\\{title[jpg.index(i)]}.jpg", 'wb')
    a.write(j.content)  # content是以二进制的方式展示
    a.close()
