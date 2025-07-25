#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 16:08
# @file: runner.py
# @project: EAI 2.0 GUI_TEST
import os
import glob
import pytest
import subprocess
from Config.Config import Config

def clean_dir(path, patterns):
    """删除指定目录下符合模式的文件"""
    if not os.path.exists(path):
        print(f"目录不存在: {path}")
        return
    for pattern in patterns:
        for file in glob.glob(os.path.join(path, pattern)):
            try:
                os.remove(file)
                print(f"已删除: {file}")
            except Exception as e:
                print(f"删除文件失败: {file} -> {e}")

def run_pytest(allure_result):
    print("开始执行pytest用例...")
    ret = pytest.main(["-v", "-s", "-p", "no:warnings", f'--alluredir={allure_result}', "--clean-alluredir"])
    if ret != 0:
        print(f"pytest 执行失败，退出码: {ret}")
    return ret

def generate_allure_report(allure_result, allure_report):
    print("开始生成Allure测试报告...")
    try:
        subprocess.run(
            ["allure", "generate", allure_result, "-o", allure_report, "--clean"],
            check=True
        )
        print(f"Allure报告已生成: {allure_report}")
    except FileNotFoundError:
        print("未找到 allure 命令，请确保已正确安装 Allure 并配置环境变量。")
    except subprocess.CalledProcessError as e:
        print(f"Allure报告生成失败: {e}")

def main():
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir

    clean_dir(Screenshot, ['*.png'])
    if run_pytest(AllureResult) == 0:
        generate_allure_report(AllureResult, AllureReport)

if __name__ == '__main__':
    main()

