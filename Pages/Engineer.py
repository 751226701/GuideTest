#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 09:03
# @file: Engineer.py
# @project: EAI_2.0_GUI_TEST
import allure
import time
from retry import retry
from Common.Common import Common

class Engineer:
    IMAGE_MAP = {
        # 工程
        "new": r"TempImage/起始窗口-新建.png",
        "open": r"TempImage/起始窗口-打开.png",
        "gc": r"TempImage/工程/工程.png",
        "gc_workpiece": r"TempImage/工程/工程-工件.png",
        "gc_robot": r"TempImage/工程/工程-机器人.png",
        "gc_robot_file": r"TempImage/工程/工程-机器人-文件.png",
        "gc_robot_confirm": r"TempImage/工程/工程-机器人-确定.png",
        "gc_robot_dropdown_irb2400": r"TempImage/工程/工程-机器人-下拉框选项-IRB2400_16.png",
        "gc_robot_dropdown_bozhong": r"TempImage/工程/工程-机器人-下拉框选项-BoZhongPolishRail.png",
        "gc_robot_world_dropdown": r"TempImage/工程/工程-机器人-world下拉框.png",
        "gc_tool": r"TempImage/工程/工程-工具.png",
        "gc_tool_hq2": r"TempImage/工程/工程-工具-HQ2.png",
        "gc_tool_confirm": r"TempImage/工程/工程-工具-确定.png",
        "gc_axis_bozhong": r"TempImage/工程/工程-附加轴-地轨-BoZhongPolishRail.png",
        "gc_axis_rail": r"TempImage/工程/工程-附加轴-地轨.png",
        "gc_axis": r"TempImage/工程/工程-附加轴.png",
        # 工程新增机器人模板
        "gc_robot_moka": r"TempImage/工程/工程-机器人-藦卡.png",
        "gc_robot_luoshi": r"TempImage/工程/工程-机器人-珞石.png",
        "gc_robot_xinsong": r"TempImage/工程/工程-机器人-新松.png",
        "gc_robot_xinshida": r"TempImage/工程/工程-机器人-新时达.png",
        "gc_robot_siling": r"TempImage/工程/工程-机器人-思灵.png",
        "gc_robot_baoyuan": r"TempImage/工程/工程-机器人-宝元.png",
        "gc_robot_qixuan": r"TempImage/工程/工程-机器人-启玄.png",
        "gc_robot_chuangmingxin": r"TempImage/工程/工程-机器人-创明鑫.png",
        "gc_robot_yaskawa": r"TempImage/工程/工程-机器人-YASKAWA.png",
        "gc_robot_ur": r"TempImage/工程/工程-机器人-UR.png",
        "gc_robot_staubli": r"TempImage/工程/工程-机器人-STAUBLI.png",
        "gc_robot_kuka": r"TempImage/工程/工程-机器人-KUKA.png",
        "gc_robot_fanuc": r"TempImage/工程/工程-机器人-FANUC.png",
        "gc_robot_efort": r"TempImage/工程/工程-机器人-EFORT.png",
        "gc_robot_aubo": r"TempImage/工程/工程-机器人-AUBO.png",
        "gc_robot_abb": r"TempImage/工程/工程-机器人-ABB.png",
        "gc_robot_abb_irb1200_5": r"TempImage/工程/工程-机器人-ABB-IRB1200_5.png",
        "gc_robot-ABB_irb2400": r"TempImage/工程/工程-机器人-ABB-IRB2400_16.png",
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
        # 断言图片
        "assert_test_case_001": r"TempImage/断言/test_case_001.png",
        "assert_test_case_002": r"TempImage/断言/test_case_002.png",
        "assert_test_case_003_1": r"TempImage/断言/test_case_003_1.png",
        "assert_test_case_003": r"TempImage/断言/test_case_003.png",
        "assert_test_case_004_1": r"TempImage/断言/test_case_004_1.png",
        "assert_test_case_004": r"TempImage/断言/test_case_004.png",
        "assert_test_case_005_1": r"TempImage/断言/test_case_005_1.png",
        "assert_test_case_005": r"TempImage/断言/test_case_005.png",
        "assert_test_case_006_1": r"TempImage/断言/test_case_006_1.png",
        "assert_test_case_006": r"TempImage/断言/test_case_006.png",
        "assert_test_case_007_1": r"TempImage/断言/test_case_007_1.png",
        "assert_test_case_007": r"TempImage/断言/test_case_007.png",
        "assert_test_case_008_1": r"TempImage/断言/test_case_008_1.png",
        "assert_test_case_008": r"TempImage/断言/test_case_008.png",
        "assert_test_case_009_1": r"TempImage/断言/test_case_009_1.png",
        "assert_test_case_009": r"TempImage/断言/test_case_009.png",
        "assert_test_case_010": r"TempImage/断言/test_case_010.png",
        "assert_test_case_011_1": r"TempImage/断言/test_case_011_1.png",
        "assert_test_case_011": r"TempImage/断言/test_case_011.png",
        "assert_test_case_012_1": r"TempImage/断言/test_case_012_1.png",
        "assert_test_case_012": r"TempImage/断言/test_case_012.png",
        "assert_test_case_013_1": r"TempImage/断言/test_case_013_1.png",
        "assert_test_case_013": r"TempImage/断言/test_case_013.png",
        "assert_test_case_014_1": r"TempImage/断言/test_case_014_1.png",
        "assert_test_case_014": r"TempImage/断言/test_case_014.png",
        "assert_test_case_015_1": r"TempImage/断言/test_case_015_1.png",
        "assert_test_case_015": r"TempImage/断言/test_case_015.png",
        "assert_test_case_016_1": r"TempImage/断言/test_case_016_1.png",
        "assert_test_case_016": r"TempImage/断言/test_case_016.png",
        "assert_test_case_017_1": r"TempImage/断言/test_case_017_1.png",
        "assert_test_case_017": r"TempImage/断言/test_case_017.png",
        "assert_test_case_018": r"TempImage/断言/test_case_018.png",
        "assert_test_case_019_1": r"TempImage/断言/test_case_019_1.png",
        "assert_test_case_019": r"TempImage/断言/test_case_019.png",
        "assert_test_case_020_1": r"TempImage/断言/test_case_020_1.png",
        "assert_test_case_020": r"TempImage/断言/test_case_020.png",
        "assert_test_case_021_1": r"TempImage/断言/test_case_021_1.png",
        "assert_test_case_021": r"TempImage/断言/test_case_021.png",
        "assert_test_case_022_1": r"TempImage/断言/test_case_022_1.png",
        "assert_test_case_022": r"TempImage/断言/test_case_022.png",
        "assert_test_case_023_1": r"TempImage/断言/test_case_023_1.png",
        "assert_test_case_023": r"TempImage/断言/test_case_023.png",
        "assert_test_case_024_1": r"TempImage/断言/test_case_024_1.png",
        "assert_test_case_024": r"TempImage/断言/test_case_024.png",
        "assert_test_case_025_1": r"TempImage/断言/test_case_025_1.png",
        "assert_test_case_025": r"TempImage/断言/test_case_025.png",
        "assert_test_case_026": r"TempImage/断言/test_case_026.png",
        "assert_test_case_027_1": r"TempImage/断言/test_case_027_1.png",
        "assert_test_case_027": r"TempImage/断言/test_case_027.png",
        "assert_test_case_028_1": r"TempImage/断言/test_case_028_1.png",
        "assert_test_case_028": r"TempImage/断言/test_case_028.png",
        "assert_test_case_029_1": r"TempImage/断言/test_case_029_1.png",
        "assert_test_case_029": r"TempImage/断言/test_case_029.png",
        "assert_test_case_030_1": r"TempImage/断言/test_case_030_1.png",
        "assert_test_case_030": r"TempImage/断言/test_case_030.png",
        "assert_test_case_031_1": r"TempImage/断言/test_case_031_1.png",
        "assert_test_case_031": r"TempImage/断言/test_case_031.png",
        "assert_test_case_032_1": r"TempImage/断言/test_case_032_1.png",
        "assert_test_case_032": r"TempImage/断言/test_case_032.png",
        "assert_test_case_033_1": r"TempImage/断言/test_case_033_1.png",
        "assert_test_case_033": r"TempImage/断言/test_case_033.png",
        "assert_test_case_034": r"TempImage/断言/test_case_034.png",
        "assert_test_case_035_1": r"TempImage/断言/test_case_035_1.png",
        "assert_test_case_035": r"TempImage/断言/test_case_035.png",
        "assert_test_case_036_1": r"TempImage/断言/test_case_036_1.png",
        "assert_test_case_036": r"TempImage/断言/test_case_036.png",
        "assert_test_case_037_1": r"TempImage/断言/test_case_037_1.png",
        "assert_test_case_037": r"TempImage/断言/test_case_037.png",
        "assert_test_case_038_1": r"TempImage/断言/test_case_038_1.png",
        "assert_test_case_038": r"TempImage/断言/test_case_038.png",
        "assert_test_case_039_1": r"TempImage/断言/test_case_039_1.png",
        "assert_test_case_039": r"TempImage/断言/test_case_039.png",
        "assert_test_case_040_1": r"TempImage/断言/test_case_040_1.png",
        "assert_test_case_040": r"TempImage/断言/test_case_040.png",
        "assert_test_case_041_1": r"TempImage/断言/test_case_041_1.png",
        "assert_test_case_041": r"TempImage/断言/test_case_041.png",
        "assert_test_case_042": r"TempImage/断言/test_case_042.png",
        "assert_test_case_043_1": r"TempImage/断言/test_case_043_1.png",
        "assert_test_case_043": r"TempImage/断言/test_case_043.png",
        "assert_test_case_044_1": r"TempImage/断言/test_case_044_1.png",
        "assert_test_case_044": r"TempImage/断言/test_case_044.png",
        "assert_test_case_045_1": r"TempImage/断言/test_case_045_1.png",
        "assert_test_case_045": r"TempImage/断言/test_case_045.png",
        "assert_test_case_046_1": r"TempImage/断言/test_case_046_1.png",
        "assert_test_case_046": r"TempImage/断言/test_case_046.png",
        "assert_test_case_047_1": r"TempImage/断言/test_case_047_1.png",
        "assert_test_case_047": r"TempImage/断言/test_case_047.png",
        "assert_test_case_048_1": r"TempImage/断言/test_case_048_1.png",
        "assert_test_case_048": r"TempImage/断言/test_case_048.png",
        "assert_test_case_049_1": r"TempImage/断言/test_case_049_1.png",
        "assert_test_case_049": r"TempImage/断言/test_case_049.png",
        "assert_test_case_050": r"TempImage/断言/test_case_50.png",
        "assert_test_case_051": r"TempImage/断言/test_case_051",
        "assert_test_case_052": r"TempImage/断言/test_case_052.png",
        "assert_test_case_053": r"TempImage/断言/test_case_053.png",
        "assert_test_case_054": r"TempImage/断言/test_case_054.png",
        "assert_test_case_055": r"TempImage/断言/test_case_055.png",
        "assert_test_case_056": r"TempImage/断言/test_case_056.png",
        "assert_test_case_057": r"TempImage/断言/test_case_057.png",
        "assert_test_case_058": r"TempImage/断言/test_case_058.png",
        "assert_test_case_059": r"TempImage/断言/test_case_059.png",
        "assert_test_case_060": r"TempImage/断言/test_case_060.png",
        "assert_test_case_061": r"TempImage/断言/test_case_061.png",
        "assert_test_case_062": r"TempImage/断言/test_case_062.png",
        "assert_test_case_063": r"TempImage/断言/test_case_063.png",
        "assert_test_case_064": r"TempImage/断言/test_case_064.png",
        "assert_test_case_065": r"TempImage/断言/test_case_065.png",
        "assert_test_case_066": r"TempImage/断言/test_case_066.png",
        "assert_test_case_067": r"TempImage/断言/test_case_067",
        "assert_test_case_068": r"TempImage/断言/test_case_068.png",
        "assert_test_case_069": r"TempImage/断言/test_case_069.png",
        "assert_test_case_070": r"TempImage/断言/test_case_070.png",
        "assert_test_case_071": r"TempImage/断言/test_case_071.png",
        "assert_test_case_072": r"TempImage/断言/test_case_072.png",
        "assert_test_case_073_1": r"TempImage/断言/test_case_073_1.png",
        "assert_test_case_073": r"TempImage/断言/test_case_073.png",
        "assert_test_case_074": r"TempImage/断言/test_case_074.png",
        "assert_test_case_075": r"TempImage/断言/test_case_075.png",
        "assert_test_case_076": r"TempImage/断言/test_case_076.png",
        "assert_test_case_077": r"TempImage/断言/test_case_077.png",
        "assert_test_case_078": r"TempImage/断言/test_case_078.png",
        "assert_test_case_079": r"TempImage/断言/test_case_079.png",
        
        
    }

    def __init__(self, common_instance=None):
        self.common = common_instance if common_instance else Common()

    @allure.step("{operation}")
    def click(self, image_key, operation, timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.wait_and_touch(image_path, operation or f"点击{image_key}",timeout=timeout, **kwargs)
    
    @allure.step("{operation}")
    def assert_exists_by_key(self, image_key, operation, timeout=10, **kwargs):
        image_path = self.IMAGE_MAP.get(image_key)
        if not image_path:
            raise ValueError(f"未找到图片关键字: {image_key}")
        self.common.assert_exists(image_path, operation or f"断言{image_key}", timeout=timeout, **kwargs)

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
        self.common.wait_and_touch(r"TempImage/工程/工程-机器人-ABB-IRB2400_16.png", "点击IRB2400_16")

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




