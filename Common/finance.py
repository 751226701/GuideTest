# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/3/13 8:46
# @File :finance
# @Project : GuideTest

import time
import tushare as ts
from Common.log import Logger

log = Logger()

def get_realtime_quotes(stock_code):
    data = ts.get_realtime_quotes(stock_code)
    print(data)


if __name__ == "__main__":
    stock_code = input("stock_code：")
    while True:
        get_realtime_quotes(stock_code)
        time.sleep(3)

# python -m PyInstaller --onefile your_script.py
