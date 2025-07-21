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
    IMAGE_MAP = {
        "new": r"TempImage/起始窗口-新建.png",
        "open": r"TempImage/起始窗口-打开.png",
        "gc": r"TempImage/工程/工程.png",
        "gc_robot": r"TempImage/工程/工程-机器人.png",
        "gc_tool": r"TempImage/工程/工程-工具.png",
        "gc_workpiece": r"TempImage/工程/工程-工件.png",
        "gc_robot_file": r"TempImage/工程/工程-机器人-文件.png",
        "gc_robot_dropdown_irb2400": r"TempImage/工程/工程-机器人-下拉框选项-IRB2400_16.png",
        "gc_tool_hq2": r"TempImage/工程/工程-工具-HQ2.png",
        "gc_tool_confirm": r"TempImage/工程/工程-工具-确定.png",
        "gc_robot_dropdown_bozhong": r"TempImage/工程/工程-机器人-下拉框选项-BoZhongPolishRail.png",
        "gc_robot_world_dropdown": r"TempImage/工程/工程-机器人-world下拉框.png",
        "gc_robot_irb2400": r"TempImage/工程/工程-机器人-IRB2400_16.png",
        "gc_axis_bozhong": r"TempImage/工程/工程-附加轴-地轨-BoZhongPolishRail.png",
        "gc_axis_rail": r"TempImage/工程/工程-附加轴-地轨.png",
        "gc_axis": r"TempImage/工程/工程-附加轴.png",
        # 工作站
        "ws_bozhong": r"TempImage/工作站/工作站-BoZhongPolishRail.png",
        "ws_move": r"TempImage/工作站/工作站-移动.png",
        "ws_move_confirm": r"TempImage/工作站/工作站-移动-确定.png",
        "ws_x": r"TempImage/工作站/站元素移动-X.png",
        "ws_y": r"TempImage/工作站/站元素移动-Y.png",
        "ws_z": r"TempImage/工作站/站元素移动-Z.png",
        "ws_xr": r"TempImage/工作站/站元素移动-XRotation.png",
        "ws_yr": r"TempImage/工作站/站元素移动-YRotation.png",
        "ws_zr": r"TempImage/工作站/站元素移动-ZRotation.png",
        # 设计
        "sj_weld": r"TempImage/设计/设计-焊接.png",
        "sj_setting": r"TempImage/设计/设计-焊接-设置.png",
        "sj_param": r"TempImage/设计/设计-焊接-参数设置.png",
        "sj_param_confirm": r"TempImage/设计/设计-焊接-参数设置-确定.png",
        "sj_param_other": r"TempImage/设计/设计-焊接-参数设置-其他.png",
        "sj_param_both": r"TempImage/设计/设计-焊接-参数设置-其他-both.png",
        "sj_param_capturing": r"TempImage/设计/设计-焊接-参数设置-其他-only capturing.png",
        "sj_param_welding": r"TempImage/设计/设计-焊接-参数设置-其他-only welding.png",
        "sj_group": r"TempImage/设计/设计-焊接-工作组.png",
        "sj_group_add": r"TempImage/设计/设计-焊接-工作组 +.png",
        "sj_group_next": r"TempImage/设计/设计-焊接-工作组 》.png",
        "sj_group_bozhong": r"TempImage/设计/设计-焊接-工作组-BoZhongPolishRail.png",
        "sj_group_save": r"TempImage/设计/设计-焊接-工作组-保存.png",
        "sj_group_linkage": r"TempImage/设计/设计-焊接-工作组-联动.png",
        "sj_collision": r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图.png",
        "sj_collision_off": r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图-碰撞地图-关.png",
    }

    def __init__(self, common_instance=None):
        self.common = common_instance if common_instance else Common()

    @allure.step("点击: {image_key}")
    def click(self, image_key, desc=None):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.wait_and_touch(image_path, desc or f"点击{image_key}")

    # ******************工程******************

    @retry(tries=3, delay=1)
    @allure.step("点击新建")
    def click_new(self):
        self.common.wait_and_touch(r"TempImage/起始窗口-新建.png", "点击新建")

    @allure.step("点击打开")
    def click_open(self):
        self.common.wait_and_touch(r"TempImage/起始窗口-打开.png", "点击打开")

    @allure.step("点击工程")
    def click_gc(self):
        self.common.wait_and_touch(r"TempImage/工程/工程.png", "点击工程")

    @allure.step("点击机器人")
    def click_gc_robot(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人.png", "点击机器人")

    @allure.step("点击工具")
    def click_gc_tool(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-工具.png", "点击工具")

    @allure.step("点击工件")
    def click_gc_workpiece(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-工件.png", "点击工件")

    @allure.step("点击文件")
    def click_gc_robot_file(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-文件.png", "点击文件")

    @allure.step("点击下拉IRB2400_16")
    def click_gc_robot_dropdown_irb2400(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-下拉框选项-IRB2400_16.png", "点击下拉IRB2400_16")

    @allure.step("点击工具HQ2")
    def click_gc_tool_hq2(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-工具-HQ2.png", "点击工具HQ2")

    @allure.step("点击工具确定")
    def click_gc_tool_confirm(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-工具-确定.png", "点击工具确定")

    @allure.step("点击下拉BoZhongPolishRail")
    def click_gc_robot_dropdown_bozhong(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-下拉框选项-BoZhongPolishRail.png", "点击下拉BoZhongPolishRail")

    @allure.step("点击world下拉")
    def click_gc_robot_world_dropdown(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-world下拉框.png", "点击world下拉")

    @allure.step("点击IRB2400_16")
    def click_gc_robot_irb2400(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-IRB2400_16.png", "点击IRB2400_16")

    @allure.step("点击地轨BoZhongPolishRail")
    def click_gc_axis_bozhong(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-附加轴-地轨-BoZhongPolishRail.png", "点击地轨BoZhongPolishRail")

    @allure.step("点击地轨")
    def click_gc_axis_rail(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-附加轴-地轨.png", "点击地轨")

    @allure.step("点击附加轴")
    def click_gc_axis(self):
        self.common.wait_and_touch(r"TempImage/工程/工程-附加轴.png", "点击附加轴")

    # ******************工作站******************

    @allure.step("点击BoZhongPolishRail")
    def click_ws_bozhong(self):
        self.common.wait_and_touch(r"TempImage/工作站/工作站-BoZhongPolishRail.png", "点击BoZhongPolishRail")

    @allure.step("点击移动")
    def click_ws_move(self):
        self.common.wait_and_touch(r"TempImage/工作站/工作站-移动.png", "点击移动")

    @allure.step("点击移动确定")
    def click_ws_move_confirm(self):
        self.common.wait_and_touch(r"TempImage/工作站/工作站-移动-确定.png", "点击移动确定")

    @allure.step("点击X")
    def click_ws_x(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-X.png", "点击X")

    @allure.step("点击Y")
    def click_ws_y(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-Y.png", "点击Y")

    @allure.step("点击Z")
    def click_ws_z(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-Z.png", "点击Z")

    @allure.step("点击X旋转")
    def click_ws_xr(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-XRotation.png", "点击X旋转")

    @allure.step("点击Y旋转")
    def click_ws_yr(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-YRotation.png", "点击Y旋转")

    @allure.step("点击Z旋转")
    def click_ws_zr(self):
        self.common.wait_and_touch(r"TempImage/工作站/站元素移动-ZRotation.png", "点击Z旋转")

    # ******************设计******************

    @allure.step("点击焊接")
    def click_sj_weld(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接.png", "点击焊接")

    @allure.step("点击设置")
    def click_sj_setting(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-设置.png", "点击设置")

    @allure.step("点击参数设置")
    def click_sj_param(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置.png", "点击参数设置")

    @allure.step("点击参数确定")
    def click_sj_param_confirm(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置-确定.png", "点击参数确定")

    @allure.step("点击参数其他")
    def click_sj_param_other(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置-其他.png", "点击参数其他")

    @allure.step("点击参数both")
    def click_sj_param_both(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置-其他-both.png", "点击参数both")

    @allure.step("点击参数capturing")
    def click_sj_param_capturing(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置-其他-only capturing.png", "点击参数capturing")

    @allure.step("点击参数welding")
    def click_sj_param_welding(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-参数设置-其他-only welding.png", "点击参数welding")

    @allure.step("点击工作组")
    def click_sj_group(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组.png", "点击工作组")

    @allure.step("点击组加号")
    def click_sj_group_add(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组 +.png", "点击组加号")

    @allure.step("点击组下一个")
    def click_sj_group_next(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组 》.png", "点击组下一个")

    @allure.step("点击组BoZhongPolishRail")
    def click_sj_group_bozhong(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组-BoZhongPolishRail.png", "点击组BoZhongPolishRail")

    @allure.step("点击组保存")
    def click_sj_group_save(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组-保存.png", "点击组保存")

    @allure.step("点击组联动")
    def click_sj_group_linkage(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-工作组-联动.png", "点击组联动")

    @allure.step("点击碰撞地图")
    def click_sj_collision(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图.png", "点击碰撞地图")

    @allure.step("点击碰撞地图关")
    def click_sj_collision_off(self):
        self.common.wait_and_touch(r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图-碰撞地图-关.png", "点击碰撞地图关")




