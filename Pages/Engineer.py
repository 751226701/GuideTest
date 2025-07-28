#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 09:03
# @file: Engineer.py
# @project: EAI_2.0_GUI_TEST
import allure
from Common.Common import Common


class Engineer:

    def __init__(self, common_instance=None):
        self.common = common_instance if common_instance else Common()
        self.IMAGE_MAP = self.common.auto_image_map()
        self.FILE_MAP = self.common.auto_file_map()

    @allure.step("{operation}")
    def click(self, image_key, operation, timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.wait_and_touch(image_path, operation or f"点击{image_key}",timeout=timeout, **kwargs)
    
    @allure.step("{operation}")
    def right_click(self, image_key, operation="", timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.right_click(image_path, operation or f"右键点击{image_key}", timeout=timeout, **kwargs)

    @allure.step("{operation}")
    def assert_exists(self, image_key, operation, timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.assert_exists(image_path, operation or f"断言{image_key}", timeout=timeout, **kwargs)

    @allure.step("{operation}")
    def input_text(self, image_key, input_str, operation="", timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.input_text(image_path, input_str, operation or f"输入{input_str}", timeout=timeout, **kwargs)

    @allure.step("{operation}")
    def swipe(self, start_pos, end_pos, operation="", duration=0.5):
        return self.common.swipe(start_pos, end_pos, operation, duration)

    @allure.step("{operation}")
    def input_file(self, file_key, operation="", **kwargs):
        file_path = self.FILE_MAP[file_key]
        if not file_path:
            raise ValueError(f"未找到文件路径: {file_key}")
        self.common.input_file(file_path, operation or f"输入文件{file_key}")
