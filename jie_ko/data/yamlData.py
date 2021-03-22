#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 13:57
# @Author : ZY
# @File : yamlData.py
# @Project : APP
import yaml


# 读
def readYaml_dict(path, key, key1):
    # "desired_capabilities.yml"
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    a = list(zip(data[f"{key}"], data[f"{key1}"]))
    return a

def readYaml_list(path):
    # "desired_capabilities.yml"
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data

# 写
def writeYaml(path, content):
    with open(path, 'w', encoding="utf-8") as f:
        yaml.dump(content, f, allow_unicode=True)
