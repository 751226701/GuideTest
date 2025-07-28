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

    exit_codes = {
        0: "所有测试用例成功通过",
        1: "有测试用例失败 (FAILED)",
        2: "测试执行过程中发生错误 (ERROR)",
        3: "测试被中断 (INTERRUPTED)",
        4: "测试收集失败 (COLLECTION_FAILED)",
        5: "测试配置错误 (USAGE_ERROR)"
    }
    
    if ret in exit_codes:
        print(f"pytest 执行完成，退出码: {ret} - {exit_codes[ret]}")
    else:
        print(f"pytest 执行完成，未知退出码: {ret}")

    if ret != 0:
        print("注意：有测试用例失败，但仍会生成Allure报告以便查看详细失败信息")
    
    return ret

def generate_allure_report(allure_result, allure_report):
    print("开始生成Allure测试报告...")
    
    cmd = f'allure generate "{allure_result}" -o "{allure_report}" --clean'
    print(f"执行命令: {cmd}")
    
    ret = os.system(cmd)
    if ret == 0:
        print(f"Allure报告已生成: {allure_report}")
        return True
    else:
        print(f"Allure报告生成失败，退出码: {ret}")
        return False

def main():
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir

    clean_dir(Screenshot, ['*.png'])
    run_pytest(AllureResult)
    generate_allure_report(AllureResult, AllureReport)
    

if __name__ == '__main__':
    main()

