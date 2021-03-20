#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/20 10:10
# @Author : ZY
# @File : Demo01_爬虫_动态.py
# @Project : code

import re
import requests

# uri = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=14.61&city=410200&geoobj=114.567698|34.804239|114.612628|34.819456&keywords=饭店'
# headers = {'Host': 'www.amap.com',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
#            'Accept': '*/*', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#            'Accept-Encoding': 'gzip, deflate, br', 'amapuuid': '4e9a107b-e865-4075-8d7b-295550e2dcea',
#            'x-csrf-token': 'null', 'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive',
#            'Referer': 'https://www.amap.com/search?query=%E9%A5%AD%E5%BA%97&city=410200&geoobj=114.351796%7C34.724163%7C114.818921%7C34.882383&zoom=11.23',
#            'Cookie': 'guid=fcdd-b311-778f-b4f6; cna=sn+OGPRE7WYCAbZ+/sg6pg/y; UM_distinctid=1771d91241393-00a3220c4ba9198-4c3f207e-e1000-1771d912414359; CNZZDATA1255626299=578732599-1611103892-https%253A%252F%252Fwww.baidu.com%252F%7C1611109293; _uab_collina=161110878731255710436025; isg=BOfn0LeoS_m-Zc91ODAf0WqwdRuxbLtOBCdQYblWDnadqAJqwT16ngHuyig2W5PG; l=eBPzSvmHjjZkhAsFBO5ZPurza77OiQAVCkPzaNbMiInca1kdEFtTqNCIZwB9mdtfgtCH9etzvffAydFe-Izdg7fZuHO1tTf7CxJO.; tfstk=c9dRBp9WQmmkMpufjLH0AQ00q_zdCENRvzsa9VvI1y-4ruWFdQ1mCCA9LDH5WZBik; xlly_s=1; x5sec=7b22617365727665723b32223a223936633730653037363232363066313661353531626363333964363332616135434962326e6f4147454d6655734f57676c4c476b52413d3d227d'}
#
# html = requests.get(uri, headers=headers)  # headers 请求头部
# # 把json数据转换成字典或列表数据
# # print(html.json())
# # print(html.json()['data']['poi_list'])
#
# for i in html.json()['data']['poi_list']:
#     print(i['disp_name'], i['tel'], i['address'])


url ='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10&city=410200&geoobj=114.231583%7C34.578548%7C114.890764%7C35.048708&keywords=%E5%AD%A6%E6%A0%A1'
a = '''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
amapuuid: c2b7117e-e68c-48c0-98f5-f69d5830c246
Connection: keep-alive
Cookie: UM_distinctid=1771d962c3c134-05e697ad7ac953-59442e11-e1000-1771d962c3d36e; cna=c8R5GJjtVwwCAbZ+/IzH0m92; _uab_collina=161179657297355229615686; CNZZDATA1255626299=1102330537-1611793248-%7C1614044879; xlly_s=1; guid=440e-e09d-de87-24eb; tfstk=cAoABdgj8QA0nxy-LqLl1pRb1UaOaRsY6tNFXpx9S-LvRZsOfsvKxD3Q-EwdMupR.; l=eBSk8J4HjjZZco6MBO5alurza77tqQOffrVzaNbMiInca6_diFs9QNCIy-OMrdtjgtfvKUtyQArmAReX-QUd0LLUiYgES3lp7xJ6-; isg=BCQknZrbGKPfl2zcfMghIENW9SIWvUgnrSGMYT5G-O-v6cOzbsw2t3gPqUFxN4B_
Host: www.amap.com
Referer: https://www.amap.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
x-csrf-token: null
X-Requested-With: XMLHttpRequest'''

d = {}
for i in a.split("\n"):
    cc = i.split(":", 1)
    d[cc[0]] = cc[1].strip()

html = requests.get(url, headers=d)  # headers 请求头部
# 把json数据转换成字典或列表数据
# print(html)  # <Response [200]>
# print(html.json())  # {'status': '1', 'searchOpt': {'city': '410200',
# print(html.json()['data']['poi_list'])

for i in html.json()['data']['poi_list']:
    print(i['disp_name'], i['tel'], i['address'])
