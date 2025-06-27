#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 16:08
# @file: runner.py
# @project: EAI 2.0 GUI_TEST

import os
import glob
import pytest
from Config.Config import Config

def clean_dir(path, patterns):
    """删除指定目录下符合模式的文件"""
    for pattern in patterns:
        for file in glob.glob(os.path.join(path, pattern)):
            try:
                os.remove(file)
            except Exception as e:
                print(f"删除文件失败: {file} -> {e}")

if __name__ == '__main__':
    # 路径准备
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir

    # 清理截图
    clean_dir(Screenshot, ['*.png'])

    # 执行用例生成测试结果
    pytest.main(["-v", "-s", "-p no:warnings",f'--alluredir={AllureResult}', "--clean-alluredir"])
    # 生成测试报告
    os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')

