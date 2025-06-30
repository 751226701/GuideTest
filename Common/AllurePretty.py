#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/23 16:05
# @file: AllurePretty.py
# @project: EAI 2.0 GUI_TEST
import os
import allure
import pytest
import functools
from Config.Config import Config
from airtest.core.api import snapshot


class PrettyAllure:
    @classmethod
    def PrettyAllureCase(cls, CaseData):
        """动态添加Allure用例信息"""
        allure.dynamic.feature(CaseData.get("模块", "未定义模块"))
        allure.dynamic.story(CaseData.get("功能", "未命名功能"))
        allure.dynamic.severity(CaseData.get("优先级", "normal"))
        allure.dynamic.title(f'{CaseData.get("用例编号")}_{CaseData.get("用例标题")}')
        if CaseData.get("是否执行") != "Y":
            allure.dynamic.description("用例指定跳过")
            pytest.skip("用例指定跳过")

    @classmethod
    def PrettyAllureScreenShot(cls, CaseData):
        # 截图路径
        save_dir = Config.test_screenshot_dir
        os.makedirs(save_dir, exist_ok=True)
        filename = os.path.join(save_dir, f"{CaseData.get("用例标题")}.png")

        # 截图并附加到Allure
        snapshot(filename)
        allure.attach.file(source = filename,name = "用例完成截图",
            attachment_type=allure.attachment_type.PNG)

    @classmethod
    def PrettyAllureWrapper(cls, func):
        """装饰器：集成用例信息+用例执行完成截图"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 1. 添加用例信息
            cls.PrettyAllureCase(CaseData=kwargs.get("CaseData"))

            try:
                result = func(*args, **kwargs)  # 执行用例
                # 2. 用例成功时添加结束截图（可选）
                cls.PrettyAllureScreenShot(CaseData=kwargs.get("CaseData"))
                return result
            except Exception:
                raise

        return wrapper