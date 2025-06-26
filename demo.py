#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/24 09:23
# @file: demo.py
# @project: EAI 2.0 GUI_TEST
import time
from pywinauto import Application
from airtest.core.api import *
from airtest.cli.parser import cli_setup

def getAllWindows(app,timeout):
    time.sleep(timeout)
    windows = app.windows()

    if not windows:
        print("未找到任何窗口！")
        return

    for window in windows:
        print(f"窗口标题: {window.window_text()}")
        print(f"窗口类名: {window.class_name()}")
        print(f"窗口句柄: {window.handle}")
        print('-' * 50)

def demo1():
    global app
    try:
        # 启动程序
        Application(backend="uia").start(r"D:\app\Hyperion\Hyper Brain WELD\HBLicenseMain.exe")
        # 连接程序
        app = Application(backend="uia").connect(path="HyperBrain.exe", timeout=10)
        # 定位到主窗口
        main_window = app.window(title_re="HyperBrain.*")
        # getAllWindows(app,6)
        # 等待主窗口就绪
        main_window.wait("visible enabled ready", timeout=10)
        # 点击新建按钮
        button = main_window.child_window(title="新建", control_type="Button")
        button.click()

        for win in app.windows():
            print(win.window_text())

        # 打印控件树
        main_window.print_control_identifiers(depth=10)

    except TimeoutError:
        print("主窗口加载超时！")
        app.kill()
    except Exception as e:
        print(f"发生异常: {e}")
        app.kill()

def demo2():
    if not cli_setup():
        auto_setup(__file__, logdir=False, devices=["Windows:///"])

    # 启动APP
    app_path = r"D:\app\Hyperion\Hyper Brain WELD\HBLicenseMain.exe"
    start_app(app_path)
    time.sleep(5)

    # 点击新建
    btn = wait(Template(r"TempImage\新建.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击附加轴
    btn = wait(Template(r"TempImage\附加轴.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击地轨
    btn = wait(Template(r"TempImage\地轨.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击焊接地轨
    btn = wait(Template(r"TempImage\焊接地轨.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击确定
    btn = wait(Template(r"TempImage\确定.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 断言焊接地轨是否添加成功
    assert_exists(Template(r"TempImage\断言焊接地轨添加成功.png", threshold=0.8, resolution=(1920, 1080)),
                  "焊接地轨添加失败")
    # 点击机器人
    btn = wait(Template(r"TempImage\机器人.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 选择机器人IRB1410
    btn = wait(Template(r"TempImage\机器人IRB14140.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击world下拉框
    btn = wait(Template(r"TempImage\world下拉框.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击BoZhongWeldRail
    btn = wait(Template(r"TempImage\BoZhongWeldRail.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击确定
    btn = wait(Template(r"TempImage\确定.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 断言机器人IRB1410添加成功
    assert_exists(Template(r"TempImage\断言机器人添加成功.png", threshold=0.8, resolution=(1920, 1080)), "机器人添加失败")
    # 点击工具
    btn = wait(Template(r"TempImage\工具.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 选择工具HQ2
    btn = wait(Template(r"TempImage\工具-HQ2.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    time.sleep(1)
    # 点击world下拉框
    btn = wait(Template(r"TempImage\world下拉框.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击IRB1410
    btn = wait(Template(r"TempImage\IRB1410.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 点击确定
    btn = wait(Template(r"TempImage\确定.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
    touch(btn)
    # 断言工具HQ2添加成功
    assert_exists(Template(r"TempImage\断言工具HQ2添加成功.png", threshold=0.8, resolution=(1920, 1080)),
                  "工具HQ2添加失败")
if __name__ == '__main__':
    demo2()