#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 09:03
# @file: Engineer.py
# @project: EAI_2.0_GUI_TEST
import allure
from airtest.core.api import *
from airtest.cli.parser import cli_setup

class Engineer:
    @allure.step("点击新建")
    def click_new(self):
        btn = wait(Template(r"TempImage\新建.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击附加轴")
    def click_additional_axis(self):
        btn = wait(Template(r"TempImage\附加轴.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击地轨")
    def click_ground_track(self):
        btn = wait(Template(r"TempImage\地轨.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击焊接地轨")
    def click_welding_ground_track(self):
        btn = wait(Template(r"TempImage\焊接地轨.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击确定")
    def click_confirm(self):
        btn = wait(Template(r"TempImage\确定.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("断言焊接地轨是否添加成功")
    def assert_welding_ground_track(self):
        assert_exists(Template(r"TempImage\断言焊接地轨添加成功.png", threshold=0.8, resolution=(1920, 1080)),"焊接地轨添加失败")

    @allure.step("点击机器人")
    def click_robot(self):
        btn = wait(Template(r"TempImage\机器人.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("选择机器人IRB14140")
    def click_robot_IRB14140(self):
        btn = wait(Template(r"TempImage\机器人IRB14140.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击world下拉框")
    def click_world_dropdown(self):
        btn = wait(Template(r"TempImage\world下拉框.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击BoZhongWeldRail")
    def click_BoZhongWeldRail(self):
        btn = wait(Template(r"TempImage\BoZhongWeldRail.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("断言机器人IRB1410添加成功")
    def assert_robot_IRB14140(self):
        assert_exists(Template(r"TempImage\断言机器人添加成功.png", threshold=0.8, resolution=(1920, 1080)), "机器人添加失败")

    @allure.step("点击工具")
    def click_tool(self):
        btn = wait(Template(r"TempImage\工具.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("选择工具HQ2")
    def click_tool_HQ2(self):
        btn = wait(Template(r"TempImage\工具-HQ2.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("点击IRB1410")
    def click_IRB1410(self):
        btn = wait(Template(r"TempImage\IRB1410.png", threshold=0.8, resolution=(1920, 1080)), timeout=10)
        touch(btn)

    @allure.step("断言工具HQ2添加成功")
    def assert_tool_HQ2(self):
        assert_exists(Template(r"TempImage\断言工具HQ2添加成功.png", threshold=0.8, resolution=(1920, 1080)), "工具HQ2添加失败")