#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 11:03
# @file: Log.py
# @project: EAI 2.0 GUI_TEST

import os
import logging
import inspect
import colorlog
from Config.Config import Config
from logging.handlers import RotatingFileHandler

LOG_PATH = Config.logs_dir    # 日志路径
PREFIX_NAME = ""              # 日志前缀名
LOG_INFO = "info.log"         # 日志名称
LOG_ERROR = "error.log"       # 日志名称


class Logger:
    def __init__(self, console_output=True, file_output=True):
        """
        :param console_output: 是否输出到控制台
        :param file_output: 是否写入到日志文件
        """
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH, exist_ok=True)

        self.info_logger = logging.getLogger("info")  # 创建info级别日志记录器
        self.error_logger = logging.getLogger("error")  # 创建error级别日志记录器

        self.info_logger.setLevel(logging.INFO)
        self.error_logger.setLevel(logging.ERROR)

        self.format = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')  # 格式化输出

        # 防止重复添加Handler
        if not self.info_logger.hasHandlers():
            if file_output:
                info_file_handler = RotatingFileHandler(
                    f"{LOG_PATH}/{PREFIX_NAME}{LOG_INFO}",
                    maxBytes=1024 * 1024 * 10,  # 每个日志文件最大10MB
                    backupCount=5  # 保留5个旧日志文件
                )
                info_file_handler.setFormatter(self.format)
                self.info_logger.addHandler(info_file_handler)

            if console_output:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)  # 控制台只输出 info 及以上
                console_formatter = colorlog.ColoredFormatter(
                    '%(log_color)s[%(asctime)s][%(levelname)s] - %(message)s',
                    log_colors={
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'bold_red',
                    }
                )
                console_handler.setFormatter(console_formatter)
                self.info_logger.addHandler(console_handler)

        if not self.error_logger.hasHandlers():
            if file_output:
                error_file_handler = RotatingFileHandler(
                    f"{LOG_PATH}/{PREFIX_NAME}{LOG_ERROR}",
                    maxBytes=1024 * 1024 * 10,  # 每个日志文件最大10MB
                    backupCount=5  # 保留5个旧日志文件
                )
                error_file_handler.setFormatter(self.format)
                self.error_logger.addHandler(error_file_handler)

            if console_output:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.ERROR)  # 控制台只输出 error 及以上
                console_formatter = colorlog.ColoredFormatter(
                    '%(log_color)s[%(asctime)s][%(levelname)s] - %(message)s',
                    log_colors={
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'bold_red',
                    }
                )
                console_handler.setFormatter(console_formatter)
                self.error_logger.addHandler(console_handler)

    def _get_caller_info(self):
        caller_frame = inspect.currentframe().f_back.f_back
        caller_filename = os.path.basename(caller_frame.f_code.co_filename)
        caller_lineno = caller_frame.f_lineno
        return f"{caller_filename}:{caller_lineno}"

    def debug(self, msg, *args, **kwargs):
        message = f"{self._get_caller_info()} - {msg}"
        self.info_logger.debug(message, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        message = f"{self._get_caller_info()} - {msg}"
        self.info_logger.info(message, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        message = f"{self._get_caller_info()} - {msg}"
        self.info_logger.warning(message, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        message = f"{self._get_caller_info()} - {msg}"
        self.error_logger.error(message, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        message = f"{self._get_caller_info()} - {msg}"
        self.error_logger.critical(message, *args, **kwargs)

_logger_instance = None

def get_logger():
    global _logger_instance
    if _logger_instance is None:
        _logger_instance = Logger()
    return _logger_instance


if __name__ == "__main__":
    log = get_logger()
    log.debug("调试信息")
    log.info("一般信息")
    log.warning("警告信息")
    log.error("错误信息")
    log.critical("严重错误信息")
