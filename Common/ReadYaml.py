#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 11:11
# @file: ReadYaml.py
# @project: EAI 2.0 GUI_TEST
import yaml
import os
from Config.Config import Config


class ReadYaml:
    def __init__(self, filename):
        self.filename = filename

    def read(self, keys=None):
        """
        返回用例列表，支持按用例编号筛选
        """
        if keys is not None and not isinstance(keys, (list, tuple)):
            raise TypeError("keys 参数必须为列表或元组")

        try:
            with open(self.filename, "r", encoding="utf8") as f:
                data_yaml = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            raise RuntimeError(f"读取 YAML 文件失败: {e}")

        if keys:
            filtered_data = [item for item in data_yaml if item.get('用例编号') in keys]
            return filtered_data
        else:
            return data_yaml


if __name__ == '__main__':
    yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
    print(yaml_data.read())
