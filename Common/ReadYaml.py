#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 11:11
# @file: ReadYaml.py
# @project: EAI 2.0 GUI_TEST
import yaml
import os
import re
from Config.Config import Config


class ReadYaml:
    def __init__(self, filename):
        self.filename = filename



    def read(self, keys=None):
        try:
            with open(self.filename, "r", encoding="utf8") as f:
                data_yaml = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            raise RuntimeError(f"读取 YAML 文件失败: {e}")



        if keys is None:
            return data_yaml
        # 单个索引
        if isinstance(keys, int):
            return data_yaml[keys]
        # 切片
        if isinstance(keys, slice):
            return data_yaml[keys]
        # 单个用例编号
        if isinstance(keys, str):
            return [item for item in data_yaml if item.get('用例编号') == keys]
        # 多个用例编号
        if isinstance(keys, (list, tuple)):
            # 判断是全int/全slice/全str
            if all(isinstance(k, int) for k in keys):
                return [data_yaml[k] for k in keys]
            elif all(isinstance(k, str) for k in keys):
                return [item for item in data_yaml if item.get('用例编号') in keys]
            else:
                raise TypeError("keys 列表只能全为int或全为str")
        raise TypeError("keys 参数类型不支持")


if __name__ == '__main__':
    yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
    # 取全部值
    # print(yaml_data.read())
    # 取索引位置值
    print(yaml_data.read(2))
    # 取切片范围值
    # print(yaml_data.read(slice(0, 2)))
    # 按用例编号取值
    # print(yaml_data.read("test_case_01"))
    # 按用例编号取多个值
    # print(yaml_data.read(["test_case_01", "test_case_02"]))
