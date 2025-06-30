#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 14:05
# @file: Config.py
# @project: EAI 2.0 GUI_TEST

import os
class Config:
    # 项目地址
    APP_PATH = r"D:\app\Hyperion\Hyperion\Hyper Brain WELD\HBLicenseMain.exe"
    APP_NAME = "HyperBrain.exe"

    # 项目根目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "TestCases"
    test_datas_dir = root_dir + os.path.sep + "TestDatas"
    test_image_dir = root_dir + os.path.sep + "TempImage"
    test_report_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"
    test_download_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Download\\"
    logs_dir = root_dir + os.path.sep + "Logs"


if __name__ == '__main__':
    print(Config.root_dir)
    print(Config.test_cases_dir)
    print(Config.test_download_dir)
    print(os.path.split(__file__))
    print(os.path.split(os.path.split(__file__)[0]))


