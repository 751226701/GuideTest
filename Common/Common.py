#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 09:02
# @file: Common.py
# @project: EAI 2.0 GUI_TEST

from datetime import datetime
from airtest.core.api import *
from airtest.core.cv import Template

class Common:
    def __init__(self,
                 threshold=0.8,
                 resolution=(1980, 1080),
                 rgb=True,
                 snapshot_dir="Logs/aieTestLog",
                 log_file="test_log.txt"):
        self.threshold = threshold
        self.resolution = resolution
        self.rgb = rgb
        self.snapshot_dir = snapshot_dir
        os.makedirs(self.snapshot_dir, exist_ok=True)
        self.log_file_path = os.path.join(self.snapshot_dir, log_file)
        self.step_counter = 0
        with open(self.log_file_path, "w", encoding="utf-8") as f:
            f.write("步骤编号\t步骤名称\t操作类型\t结果\t开始时间\t结束时间\t耗时(s)\t备注\n")

    def log_step(self, step_name, op_type, result, start_time, end_time, msg=""):
        duration = round(end_time - start_time, 3)
        start_str = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
        end_str = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file_path, "a", encoding="utf-8") as f:
            f.write(f"{self.step_counter}\t{step_name}\t{op_type}\t{result}\t{start_str}\t{end_str}\t{duration}\t{msg}\n")

    def snapshot(self, filename: str, msg: str = "") -> str:
        filepath = os.path.join(self.snapshot_dir, filename)
        snapshot(filename=filepath, msg=msg)
        return filepath  # 返回截图完整路径

    def create_template(self,
                        img,
                        record_pos=None,
                        resolution=None,
                        threshold=None,
                        rgb=None,
                        target_pos=None,):
        return Template(
            img,
            record_pos=record_pos,
            resolution=resolution if resolution is not None else self.resolution,
            threshold=threshold if threshold is not None else self.threshold,
            rgb=rgb if rgb is not None else self.rgb,
            target_pos=target_pos,)

    def wait_and_touch(self, image_path: str, step_name: str, timeout=10,
                       record_pos=None, resolution=None, threshold=None, rgb=None,
                       target_pos=None) -> str:
        """
        :param image_path: 模板图路径，支持相对路径或绝对路径，通常为 .png 文件。
        :param step_name: 当前操作的步骤名称，用于日志记录和截图命名，建议简短有描述性。
        :param timeout: 等待模板图匹配的超时时间（单位：秒），默认值为 10 秒。
        :param record_pos: 录制时的坐标位置（由 Airtest IDE 自动生成，可选）。
        :param resolution: 模板录制时的屏幕分辨率，默认使用 Common 类中设定的 resolution。
        :param threshold: 图像匹配的相似度阈值，范围 [0, 1]，默认 0.9，值越大匹配越精确。
        :param rgb: 是否使用 RGB 三通道匹配，默认为 True，适用于彩色图像识别。
        :param target_pos: 点击时的相对坐标位置（如 "center"、"left"、"right"），默认为 None。
        :return: 无显式返回，若识别失败则抛出异常；成功时执行对应操作并记录日志。
        """
        self.step_counter += 1
        tpl = self.create_template(image_path, record_pos, resolution, threshold, rgb, target_pos)
        print(f"[INFO] Step {self.step_counter}: 等待并点击 '{step_name}' -> {image_path}")
        start_time = time.time()
        try:
            wait(tpl, timeout=timeout)
            before_path = self.snapshot(f"{self.step_counter}_{step_name}_before.png", msg=f"{step_name} 前")
            touch(tpl)
            after_path = self.snapshot(f"{self.step_counter}_{step_name}_after.png", msg=f"{step_name} 后")
            result = "成功"
        except Exception as e:
            fail_path = self.snapshot(f"{self.step_counter}_{step_name}_failed.png", msg=f"{step_name} 失败")
            result = f"失败: {str(e)}"
            raise e
        end_time = time.time()
        self.log_step(step_name, "wait_and_touch", result, start_time, end_time)
        return after_path  # 返回成功后截图路径


    def swipe(self, start_pos, end_pos, duration=0.5, step_name="滑动") -> str:
        self.step_counter += 1
        print(f"[INFO] Step {self.step_counter}: 滑动操作 '{step_name}' 从 {start_pos} 到 {end_pos}")
        start_time = time.time()
        try:
            swipe(start_pos, end_pos, duration=duration)
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}.png", msg=f"{step_name} 滑动截图")
            result = "成功"
        except Exception as e:
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}_failed.png", msg=f"{step_name} 滑动失败")
            result = f"失败: {str(e)}"
            raise e
        end_time = time.time()
        self.log_step(step_name, "swipe", result, start_time, end_time)
        return snap_path

    def input_text(self, image_path, text_input, step_name, timeout=10,
                   record_pos=None, resolution=None, threshold=None, rgb=None,
                   target_pos=None) -> str:
        self.step_counter += 1
        tpl = self.create_template(image_path, record_pos, resolution, threshold, rgb, target_pos)
        print(f"[INFO] Step {self.step_counter}: 输入文本 '{text_input}' 到 '{step_name}'")
        start_time = time.time()
        try:
            wait(tpl, timeout=timeout)
            touch(tpl)
            text(text_input, enter=False)
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}_input.png", msg=f"{step_name} 输入完成")
            result = "成功"
        except Exception as e:
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}_failed.png", msg=f"{step_name} 输入失败")
            result = f"失败: {str(e)}"
            raise e
        end_time = time.time()
        self.log_step(step_name, "input_text", result, start_time, end_time)
        return snap_path

    def assert_exists(self, image_path, step_name, timeout=10,
                      record_pos=None, resolution=None, threshold=None, rgb=None,
                      target_pos=None) -> str:
        self.step_counter += 1
        tpl = self.create_template(image_path, record_pos, resolution, threshold, rgb, target_pos)
        print(f"[INFO] Step {self.step_counter}: 断言存在 '{step_name}' -> {image_path}")
        start_time = time.time()
        try:
            wait(tpl, timeout=timeout)
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}_assert.png", msg=f"{step_name} 存在断言截图")
            result = "存在"
        except Exception as e:
            snap_path = self.snapshot(f"{self.step_counter}_{step_name}_assert_failed.png", msg=f"{step_name} 断言失败")
            result = "不存在"
            raise AssertionError(f"断言失败: 模板'{step_name}'不存在")
        end_time = time.time()
        self.log_step(step_name, "assert_exists", result, start_time, end_time)
        return snap_path
