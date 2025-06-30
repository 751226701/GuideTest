#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 10:04
# @file: conftest.py
# @project: EAI_2.0_GUI_TEST
import pytest
import logging
import allure
import psutil
from airtest.core.api import *
from Config.Config import Config
from Config.Config import Config
logging.getLogger("airtest").setLevel(logging.WARNING)


@pytest.fixture(scope="class")
def gui_app():
    auto_setup(__file__, logdir=False, devices=["Windows:///"])
    kill_process_by_name(Config.APP_NAME)

    try:
        with allure.step("启动应用"):
            start_app(Config.APP_PATH)
            time.sleep(5)  # 等待稳定
            snapshot_name = "app_launch.png"
            snapshot_path = os.path.join(Config.test_screenshot_dir, snapshot_name)
            snapshot(snapshot_path)
            allure.attach.file(snapshot_path, name="应用启动截图",attachment_type=allure.attachment_type.PNG)

        yield  # 测试执行

    finally:
        # 无论测试成功/失败，最后关闭应用
        with allure.step("关闭应用"):
            kill_process_by_name(Config.APP_NAME)
            snapshot_name = "app_exit.png"
            snapshot_path = os.path.join(Config.test_screenshot_dir, snapshot_name)
            snapshot(snapshot_path)
            allure.attach.file(snapshot_path, name="应用退出截图",attachment_type=allure.attachment_type.PNG)


def kill_process_by_name(process_name):
    """强制结束指定进程"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.kill()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """自动捕获失败截图并附加到Allure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 生成唯一文件名：用例名 + 时间戳
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{item.name}_fail_{timestamp}.png"
        screenshot_path = os.path.join(Config.test_screenshot_dir, screenshot_name)

        # 确保目录存在
        os.makedirs(Config.test_screenshot_dir, exist_ok=True)

        # 截图并附加到Allure
        snapshot(screenshot_path)
        allure.attach.file(source=screenshot_path, name=f"{item.name} 失败截图",
            attachment_type=allure.attachment_type.PNG)

