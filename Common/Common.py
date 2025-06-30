#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 09:02
# @file: Common.py
# @project: EAI 2.0 GUI_TEST
from datetime import datetime
import allure
from airtest.core.api import *
from airtest.core.cv import Template
import time
import os
import queue
import threading


class AsyncLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_queue = queue.Queue()
        self._running = True
        self.worker = threading.Thread(target=self._write_worker, daemon=True)
        self.worker.start()

        # 确保目录存在
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        # 写入CSV头
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("step_id,operation,status,duration_ms,timestamp,message\n")

    def _write_worker(self):
        """异步写入工作线程"""
        while self._running or not self.log_queue.empty():
            try:
                with open(self.log_file, "a", encoding="utf-8") as f:
                    while not self.log_queue.empty():
                        f.write(self.log_queue.get_nowait())
                time.sleep(0.1)  # 控制写入频率
            except Exception as e:
                print(f"[Logger Error] {str(e)}")

    def log(self, record):
        """线程安全的日志记录"""
        self.log_queue.put(record)

    def stop(self):
        """停止日志线程"""
        self._running = False
        self.worker.join()


class Common:
    def __init__(self,
                 threshold=0.8,
                 resolution=(1920, 1080),
                 target_pos=5,
                 rgb=False,
                 log_dir="Logs"):

        self.threshold = threshold
        self.resolution = resolution
        self.target_pos= target_pos
        self.rgb = rgb
        self.step_counter = 0
        self.logger = AsyncLogger(os.path.join(log_dir, "airtest_log.csv"))

    def _log_operation(self, operation, status, duration, message=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{self.step_counter},{operation},{status},{duration:.0f},{timestamp},{message}\n"
        self.logger.log(log_entry)

    def wait_and_touch(self, image_path, operation="", timeout=10, **kwargs):
        with allure.step(operation):
            self.step_counter += 1
            start_time = time.perf_counter()

            try:
                tpl = Template(
                    image_path,
                    threshold=kwargs.get("threshold", self.threshold),
                    record_pos=kwargs.get("record_pos"),
                    resolution=kwargs.get("resolution", self.resolution),
                    rgb=kwargs.get("rgb", self.rgb),
                    target_pos=kwargs.get("target_pos", self.target_pos)
                )
                pos = wait(tpl, timeout=timeout)
                touch(pos)

                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "SUCCESS", duration)
                return duration

            except Exception as e:
                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "FAILED", duration, str(e))
                raise

    def swipe(self, start_pos, end_pos, operation="", duration=0.5):
        with allure.step(operation):
            self.step_counter += 1
            start_time = time.perf_counter()

            try:
                swipe(start_pos, end_pos, duration=duration)
                op_duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "SUCCESS", op_duration)
                return op_duration
            except Exception as e:
                op_duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "FAILED", op_duration, str(e))
                raise

    def input_text(self, image_path, text, operation="", timeout=10, **kwargs):
        with allure.step(operation):
            self.step_counter += 1
            start_time = time.perf_counter()

            try:
                tpl = Template(
                    image_path,
                    threshold=kwargs.get("threshold", self.threshold),
                    record_pos=kwargs.get("record_pos"),
                    resolution=kwargs.get("resolution", self.resolution),
                    rgb=kwargs.get("rgb", self.rgb),
                    target_pos=kwargs.get("target_pos", self.target_pos)
                )
                pos = wait(tpl, timeout=timeout)
                touch(pos)
                text(str(text), enter=False)

                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "SUCCESS", duration)
                return duration
            except Exception as e:
                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "FAILED", duration, str(e))
                raise

    def assert_exists(self, image_path, operation="", timeout=10, **kwargs):
        with allure.step(operation):
            self.step_counter += 1
            start_time = time.perf_counter()

            try:
                tpl = Template(
                    image_path,
                    threshold=kwargs.get("threshold", self.threshold),
                    record_pos=kwargs.get("record_pos"),
                    resolution=kwargs.get("resolution", self.resolution),
                    rgb=kwargs.get("rgb", self.rgb),
                    target_pos=kwargs.get("target_pos", self.target_pos)
                )
                wait(tpl, timeout=timeout)
                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "ASSERT_PASS", duration)
                return duration
            except Exception as e:
                duration = (time.perf_counter() - start_time) * 1000
                self._log_operation(operation, "ASSERT_FAIL", duration, str(e))
                raise AssertionError(f"元素不存在: {image_path}")

    def __del__(self):
        """析构时确保日志线程安全退出"""
        self.logger.stop()