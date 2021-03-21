#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/20 16:13
# @Author : ZY
# @File : conftest.py
# @Project : jie_ko

import pytest
import json
import requests
from data.yamlData import readYaml
from common.basePage import LogHandler
logger = LogHandler.logger


# 接口自动化
@pytest.fixture(params=readYaml("../data/key_chars.yaml"))
def biaozhendianma(request):
    logger.error(f"当前测试的是key={request.param[0]}，chars={request.param[1]}")
    # print(f"\n当前测试的是key={request.param[0]}，chars={request.param[1]}")
    url = "http://v.juhe.cn/cccn/to_telecodes.php"
    para = f"key={request.param[0]}&chars={request.param[1]}"  # 参数
    # get请求时，参数要传给params
    res = requests.get(url, params=para)
    return res, request.param[0], request.param[1]


def jiami(x):
    return "20" + oct(int(str(x)[2:]) * 1000)[2:]


def bai():
    url = "http://192.168.10.44:6088"
    # post请求时，带上content-type字段,头部字段传给headers
    head = {"Content-Type": "application/json"}
    para = {"name": "博文", "no": jiami(201102)}
    # 把pare数据格式变成json格式
    para = json.dumps(para).encode("utf-8")
    # post请求时，参数要传给data
    res = requests.post(url, headers=head, data=para).json()
    print(res)
    print(type(res))
    return res


if __name__ == '__main__':
    bai()
