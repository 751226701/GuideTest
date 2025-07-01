#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 09:03
# @file: Engineer.py
# @project: EAI_2.0_GUI_TEST
import allure
from retry import retry
from Common.Common import Common

class Engineer:
    def __init__(self, common_instance=None):
        self.common = common_instance if common_instance else Common()

    @retry(tries=3, delay=1)
    @allure.step("点击新建")
    def click_new(self):
        self.common.wait_and_touch(r"TempImage\新建.png", "点击新建")

    @allure.step("点击附加轴")
    def click_additional_axis(self):
        self.common.wait_and_touch(r"TempImage\附加轴.png", "点击附加轴")

    @allure.step("点击地轨")
    def click_ground_track(self):
        self.common.wait_and_touch(r"TempImage\地轨.png", "点击地轨")

    @allure.step("点击焊接地轨")
    def click_welding_ground_track(self):
        self.common.wait_and_touch(r"TempImage\焊接地轨.png", "点击焊接地轨")

    @allure.step("点击确定")
    def click_confirm(self):
        self.common.wait_and_touch(r"TempImage\确定.png", "点击确定")

    @allure.step("断言焊接地轨是否添加成功")
    def assert_welding_ground_track(self):
        self.common.assert_exists(r"TempImage\断言焊接地轨添加成功.png", "断言焊接地轨是否添加成功")

    @allure.step("点击机器人")
    def click_robot(self):
        self.common.wait_and_touch(r"TempImage\机器人.png", "点击机器人")

    @allure.step("选择机器人IRB14140")
    def click_robot_IRB14140(self):
        self.common.wait_and_touch(r"TempImage\机器人IRB14140.png", "选择机器人IRB14140")

    @allure.step("点击world下拉框")
    def click_world_dropdown(self):
        self.common.wait_and_touch(r"TempImage\world下拉框.png", "点击world下拉框")

    @allure.step("点击BoZhongWeldRail")
    def click_BoZhongWeldRail(self):
        self.common.wait_and_touch(r"TempImage\BoZhongWeldRail.png", "点击BoZhongWeldRail")

    @allure.step("断言机器人IRB1410添加成功")
    def assert_robot_IRB14140(self):
        self.common.assert_exists(r"TempImage\断言机器人添加成功.png", "断言机器人IRB1410添加成功")

    @allure.step("点击工具")
    def click_tool(self):
        self.common.wait_and_touch(r"TempImage\工具.png", "点击工具")

    @allure.step("点击工具HQ2")
    def click_tool_HQ2(self):
        self.common.wait_and_touch(r"TempImage\工具-HQ2.png", "点击工具HQ2")

    @allure.step("点击IRB1410")
    def click_IRB1410(self):
        self.common.wait_and_touch(r"TempImage\IRB1410.png", "点击IRB1410")

    @allure.step("断言工具HQ2添加成功")
    def assert_tool_HQ2(self):
        self.common.assert_exists(r"TempImage\断言工具HQ2添加成功.png", "断言工具HQ2添加成功")