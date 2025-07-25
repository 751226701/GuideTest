#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 刘涛
# @time: 2025/6/26 09:03
# @file: Engineer.py
# @project: EAI_2.0_GUI_TEST
import allure
import time
import os
from Config.Config import Config
from retry import retry
from Common.Common import Common

def auto_image_map(root_dir=Config.template_dir):
    image_map = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.png'):
                name_no_ext = os.path.splitext(filename)[0]
                rel_path = os.path.join(dirpath, filename).replace("\\", "/")
                image_map[name_no_ext] = rel_path
    return image_map

class Engineer:
    # IMAGE_MAP = {
    #     "new": r"TempImage/新建.png",
    #     "open": r"TempImage/打开.png",
    #     # 开始
    #     "ks": r"TempImage/开始/开始.png",
    #     "ks_home": r"TempImage/开始/开始-主页.png",
    #     "ks_design": r"TempImage/开始/开始-设计.png",
    #     "ks_design_cancel": r"TempImage/开始/开始-设计-取消.png",
    #     # 工程
    #     "gc": r"TempImage/工程/工程.png",
    #     "gc_workpiece": r"TempImage/工程/工程-工件.png",
    #     "gc_robot": r"TempImage/工程/工程-机器人.png",
    #     "gc_robot_xx": r"TempImage/工程/工程-机器人-xx.png",
    #     "gc_robot_cancel": r"TempImage/工程/工程-机器人-取消.png",
    #     "gc_robot_file": r"TempImage/工程/工程-机器人-文件.png",
    #     "gc_robot_file_open": r"TempImage/工程/工程-机器人-文件-打开.png",
    #     "gc_robot_confirm": r"TempImage/工程/工程-机器人-确定.png",
    #     "gc_robot_dropdown_irb2400": r"TempImage/工程/工程-机器人-下拉框选项-IRB2400_16.png",
    #     "gc_robot_dropdown_bozhong": r"TempImage/工程/工程-机器人-下拉框选项-BoZhongPolishRail.png",
    #     "gc_robot_world_dropdown": r"TempImage/工程/工程-机器人-world下拉框.png",
    #     "gc_tool": r"TempImage/工程/工程-工具.png",
    #     "gc_tool_hq2": r"TempImage/工程/工程-工具-HQ2.png",
    #     "gc_tool_confirm": r"TempImage/工程/工程-工具-确定.png",
    #     "gc_axis_bozhong": r"TempImage/工程/工程-附加轴-地轨-BoZhongPolishRail.png",
    #     "gc_axis_rail": r"TempImage/工程/工程-附加轴-地轨.png",
    #     "gc_axis": r"TempImage/工程/工程-附加轴.png",
    #     "gc_robot_abb_slider_top": r"TempImage/工程/工程-机器人-ABB-滑动条上箭头.png",
    #     "gc_robot_abb_slider_bottom": r"TempImage/工程/工程-机器人-ABB-滑动条下箭头.png",
    #     # 工程新增机器人模板
    #     "gc_robot_moka": r"TempImage/工程/工程-机器人-藦卡.png",
    #     "gc_robot_moka_mr12_2010": r"TempImage/工程/工程-机器人-藦卡-MR12-2010.png",
    #     "gc_robot_luoshi": r"TempImage/工程/工程-机器人-珞石.png",
    #     "gc_robot_luoshi_nb12_12": r"TempImage/工程/工程-机器人-珞石-NB12-12.png",
    #     "gc_robot_xinsong": r"TempImage/工程/工程-机器人-新松.png",
    #     "gc_robot_xinsong_gcr14_1400": r"TempImage/工程/工程-机器人-新松-GCR14-1400.png",
    #     "gc_robot_xinshida": r"TempImage/工程/工程-机器人-新时达.png",
    #     "gc_robot_xinshida_sr20": r"TempImage/工程/工程-机器人-新时达-SR20.png",
    #     "gc_robot_siling": r"TempImage/工程/工程-机器人-思灵.png",
    #     "gc_robot_siling_diana7": r"TempImage/工程/工程-机器人-思灵-Diana7.png",
    #     "gc_robot_baoyuan": r"TempImage/工程/工程-机器人-宝元.png",
    #     "gc_robot_baoyuan_r6_0616w": r"TempImage/工程/工程-机器人-宝元-R6-0616W.png",
    #     "gc_robot_qixuan": r"TempImage/工程/工程-机器人-启玄.png",
    #     "gc_robot_qixuan_1500": r"TempImage/工程/工程-机器人-启玄-qixuan-1500.png",
    #     "gc_robot_chuangmingxin": r"TempImage/工程/工程-机器人-创明鑫.png",
    #     "gc_robot_chuangmingxin_mx1440h_l6": r"TempImage/工程/工程-机器人-创明鑫-MX1440H-L6.png",
    #     "gc_robot_yaskawa": r"TempImage/工程/工程-机器人-YASKAWA.png",
    #     "gc_robot_yaskawa_epx2050": r"TempImage/工程/工程-机器人-YASKAWA-EPX2050.png",
    #     "gc_robot_ur": r"TempImage/工程/工程-机器人-UR.png",
    #     "gc_robot_ur_ur10": r"TempImage/工程/工程-机器人-UR-UR10.png",
    #     "gc_robot_staubli": r"TempImage/工程/工程-机器人-STAUBLI.png",
    #     "gc_robot_staubli_rx160": r"TempImage/工程/工程-机器人-STAUBLI-RX160.png",
    #     "gc_robot_kuka": r"TempImage/工程/工程-机器人-KUKA.png",
    #     "gc_robot_kuka_kr10_r1420": r"TempImage/工程/工程-机器人-KUKA-KR10 R1420.png",
    #     "gc_robot_fanuc": r"TempImage/工程/工程-机器人-FANUC.png",
    #     "gc_robot_fanuc_lr200id7l": r"TempImage/工程/工程-机器人-FANUC-LR Mate 200iD7L.png",
    #     "gc_robot_efort": r"TempImage/工程/工程-机器人-EFORT.png",
    #     "gc_robot_efort_acr12_2000": r"TempImage/工程/工程-机器人-EFORT-ACR12-2000.png",
    #     "gc_robot_aubo": r"TempImage/工程/工程-机器人-AUBO.png",
    #     "gc_robot_aubo_aubo-i10": r"TempImage/工程/工程-机器人-AUBO-AUBO-i10.png",
    #     "gc_robot_abb": r"TempImage/工程/工程-机器人-ABB.png",
    #     "gc_robot_abb_irb1200_5": r"TempImage/工程/工程-机器人-ABB-IRB1200_5.png",
    #     "gc_robot_abb_irb2400": r"TempImage/工程/工程-机器人-ABB-IRB2400_16.png",
    #     "gc_robot_x": r"TempImage/工程/工程-机器人-X.png",
    #     "gc_robot_y": r"TempImage/工程/工程-机器人-Y.png",
    #     "gc_robot_z": r"TempImage/工程/工程-机器人-Z.png",
    #     "gc_robot_Rx": r"TempImage/工程/工程-机器人-Rx.png",
    #     "gc_robot_Ry": r"TempImage/工程/工程-机器人-Ry.png",
    #     "gc_robot_Rz": r"TempImage/工程/工程-机器人-Rz.png",
    #     # 工作站
    #     "ws": r"TempImage/工作站/工作站.png",
    #     "ws_robot_IRB1200_5": r"TempImage/工作站/工作站-机器人-IRB1200_5.png",
    #     "ws_robot_delete": r"TempImage/工作站/工作站-机器人-删除.png",
    #     "ws_bozhong": r"TempImage/工作站/工作站-BoZhongPolishRail.png",
    #     "ws_move": r"TempImage/工作站/工作站-移动.png",
    #     "ws_move_confirm": r"TempImage/工作站/工作站-移动-确定.png",
    #     "ws_x": r"TempImage/工作站/站元素移动-X.png",
    #     "ws_y": r"TempImage/工作站/站元素移动-Y.png",
    #     "ws_z": r"TempImage/工作站/站元素移动-Z.png",
    #     "ws_xr": r"TempImage/工作站/站元素移动-XRotation.png",
    #     "ws_yr": r"TempImage/工作站/站元素移动-YRotation.png",
    #     "ws_zr": r"TempImage/工作站/站元素移动-ZRotation.png",
    #     # 设计
    #     "sj_weld": r"TempImage/设计/设计-焊接.png",
    #     "sj_setting": r"TempImage/设计/设计-焊接-设置.png",
    #     "sj_param": r"TempImage/设计/设计-焊接-参数设置.png",
    #     "sj_param_confirm": r"TempImage/设计/设计-焊接-参数设置-确定.png",
    #     "sj_param_other": r"TempImage/设计/设计-焊接-参数设置-其他.png",
    #     "sj_param_both": r"TempImage/设计/设计-焊接-参数设置-其他-both.png",
    #     "sj_param_capturing": r"TempImage/设计/设计-焊接-参数设置-其他-only capturing.png",
    #     "sj_param_welding": r"TempImage/设计/设计-焊接-参数设置-其他-only welding.png",
    #     "sj_group": r"TempImage/设计/设计-焊接-工作组.png",
    #     "sj_group_add": r"TempImage/设计/设计-焊接-工作组 +.png",
    #     "sj_group_next": r"TempImage/设计/设计-焊接-工作组 》.png",
    #     "sj_group_bozhong": r"TempImage/设计/设计-焊接-工作组-BoZhongPolishRail.png",
    #     "sj_group_save": r"TempImage/设计/设计-焊接-工作组-保存.png",
    #     "sj_group_linkage": r"TempImage/设计/设计-焊接-工作组-联动.png",
    #     "sj_collision": r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图.png",
    #     "sj_collision_off": r"TempImage/设计/设计-焊接-焊缝设置-碰撞地图-碰撞地图-关.png",
    #     # 断言图片
    #     "assert_test_case_001": r"TempImage/断言/test_case_001.png",
    #     "assert_test_case_002": r"TempImage/断言/test_case_002.png",
    #     "assert_test_case_003_1": r"TempImage/断言/test_case_003_1.png",
    #     "assert_test_case_003": r"TempImage/断言/test_case_003.png",
    #     "assert_test_case_004_1": r"TempImage/断言/test_case_004_1.png",
    #     "assert_test_case_004": r"TempImage/断言/test_case_004.png",
    #     "assert_test_case_005_1": r"TempImage/断言/test_case_005_1.png",
    #     "assert_test_case_005": r"TempImage/断言/test_case_005.png",
    #     "assert_test_case_006_1": r"TempImage/断言/test_case_006_1.png",
    #     "assert_test_case_006": r"TempImage/断言/test_case_006.png",
    #     "assert_test_case_007_1": r"TempImage/断言/test_case_007_1.png",
    #     "assert_test_case_007": r"TempImage/断言/test_case_007.png",
    #     "assert_test_case_008_1": r"TempImage/断言/test_case_008_1.png",
    #     "assert_test_case_008": r"TempImage/断言/test_case_008.png",
    #     "assert_test_case_009_1": r"TempImage/断言/test_case_009_1.png",
    #     "assert_test_case_009": r"TempImage/断言/test_case_009.png",
    #     "assert_test_case_010": r"TempImage/断言/test_case_010.png",
    #     "assert_test_case_011_1": r"TempImage/断言/test_case_011_1.png",
    #     "assert_test_case_011": r"TempImage/断言/test_case_011.png",
    #     "assert_test_case_012_1": r"TempImage/断言/test_case_012_1.png",
    #     "assert_test_case_012": r"TempImage/断言/test_case_012.png",
    #     "assert_test_case_013_1": r"TempImage/断言/test_case_013_1.png",
    #     "assert_test_case_013": r"TempImage/断言/test_case_013.png",
    #     "assert_test_case_014_1": r"TempImage/断言/test_case_014_1.png",
    #     "assert_test_case_014": r"TempImage/断言/test_case_014.png",
    #     "assert_test_case_015_1": r"TempImage/断言/test_case_015_1.png",
    #     "assert_test_case_015": r"TempImage/断言/test_case_015.png",
    #     "assert_test_case_016_1": r"TempImage/断言/test_case_016_1.png",
    #     "assert_test_case_016": r"TempImage/断言/test_case_016.png",
    #     "assert_test_case_017_1": r"TempImage/断言/test_case_017_1.png",
    #     "assert_test_case_017": r"TempImage/断言/test_case_017.png",
    #     "assert_test_case_018": r"TempImage/断言/test_case_018.png",
    #     "assert_test_case_019_1": r"TempImage/断言/test_case_019_1.png",
    #     "assert_test_case_019": r"TempImage/断言/test_case_019.png",
    #     "assert_test_case_020_1": r"TempImage/断言/test_case_020_1.png",
    #     "assert_test_case_020": r"TempImage/断言/test_case_020.png",
    #     "assert_test_case_021_1": r"TempImage/断言/test_case_021_1.png",
    #     "assert_test_case_021": r"TempImage/断言/test_case_021.png",
    #     "assert_test_case_022_1": r"TempImage/断言/test_case_022_1.png",
    #     "assert_test_case_022": r"TempImage/断言/test_case_022.png",
    #     "assert_test_case_023_1": r"TempImage/断言/test_case_023_1.png",
    #     "assert_test_case_023": r"TempImage/断言/test_case_023.png",
    #     "assert_test_case_024_1": r"TempImage/断言/test_case_024_1.png",
    #     "assert_test_case_024": r"TempImage/断言/test_case_024.png",
    #     "assert_test_case_025_1": r"TempImage/断言/test_case_025_1.png",
    #     "assert_test_case_025": r"TempImage/断言/test_case_025.png",
    #     "assert_test_case_026": r"TempImage/断言/test_case_026.png",
    #     "assert_test_case_027_1": r"TempImage/断言/test_case_027_1.png",
    #     "assert_test_case_027": r"TempImage/断言/test_case_027.png",
    #     "assert_test_case_028_1": r"TempImage/断言/test_case_028_1.png",
    #     "assert_test_case_028": r"TempImage/断言/test_case_028.png",
    #     "assert_test_case_029_1": r"TempImage/断言/test_case_029_1.png",
    #     "assert_test_case_029": r"TempImage/断言/test_case_029.png",
    #     "assert_test_case_030_1": r"TempImage/断言/test_case_030_1.png",
    #     "assert_test_case_030": r"TempImage/断言/test_case_030.png",
    #     "assert_test_case_031_1": r"TempImage/断言/test_case_031_1.png",
    #     "assert_test_case_031": r"TempImage/断言/test_case_031.png",
    #     "assert_test_case_032_1": r"TempImage/断言/test_case_032_1.png",
    #     "assert_test_case_032": r"TempImage/断言/test_case_032.png",
    #     "assert_test_case_033_1": r"TempImage/断言/test_case_033_1.png",
    #     "assert_test_case_033": r"TempImage/断言/test_case_033.png",
    #     "assert_test_case_034": r"TempImage/断言/test_case_034.png",
    #     "assert_test_case_035_1": r"TempImage/断言/test_case_035_1.png",
    #     "assert_test_case_035": r"TempImage/断言/test_case_035.png",
    #     "assert_test_case_036_1": r"TempImage/断言/test_case_036_1.png",
    #     "assert_test_case_036": r"TempImage/断言/test_case_036.png",
    #     "assert_test_case_037_1": r"TempImage/断言/test_case_037_1.png",
    #     "assert_test_case_037": r"TempImage/断言/test_case_037.png",
    #     "assert_test_case_038_1": r"TempImage/断言/test_case_038_1.png",
    #     "assert_test_case_038": r"TempImage/断言/test_case_038.png",
    #     "assert_test_case_039_1": r"TempImage/断言/test_case_039_1.png",
    #     "assert_test_case_039": r"TempImage/断言/test_case_039.png",
    #     "assert_test_case_040_1": r"TempImage/断言/test_case_040_1.png",
    #     "assert_test_case_040": r"TempImage/断言/test_case_040.png",
    #     "assert_test_case_041_1": r"TempImage/断言/test_case_041_1.png",
    #     "assert_test_case_041": r"TempImage/断言/test_case_041.png",
    #     "assert_test_case_042": r"TempImage/断言/test_case_042.png",
    #     "assert_test_case_043_1": r"TempImage/断言/test_case_043_1.png",
    #     "assert_test_case_043": r"TempImage/断言/test_case_043.png",
    #     "assert_test_case_044_1": r"TempImage/断言/test_case_044_1.png",
    #     "assert_test_case_044": r"TempImage/断言/test_case_044.png",
    #     "assert_test_case_045_1": r"TempImage/断言/test_case_045_1.png",
    #     "assert_test_case_045": r"TempImage/断言/test_case_045.png",
    #     "assert_test_case_046_1": r"TempImage/断言/test_case_046_1.png",
    #     "assert_test_case_046": r"TempImage/断言/test_case_046.png",
    #     "assert_test_case_047_1": r"TempImage/断言/test_case_047_1.png",
    #     "assert_test_case_047": r"TempImage/断言/test_case_047.png",
    #     "assert_test_case_048_1": r"TempImage/断言/test_case_048_1.png",
    #     "assert_test_case_048": r"TempImage/断言/test_case_048.png",
    #     "assert_test_case_049_1": r"TempImage/断言/test_case_049_1.png",
    #     "assert_test_case_049": r"TempImage/断言/test_case_049.png",
    #     "assert_test_case_050": r"TempImage/断言/test_case_050.png",
    #     "assert_test_case_051": r"TempImage/断言/test_case_051",
    #     "assert_test_case_052": r"TempImage/断言/test_case_052.png",
    #     "assert_test_case_053": r"TempImage/断言/test_case_053.png",
    #     "assert_test_case_054": r"TempImage/断言/test_case_054.png",
    #     "assert_test_case_055": r"TempImage/断言/test_case_055.png",
    #     "assert_test_case_056": r"TempImage/断言/test_case_056.png",
    #     "assert_test_case_057": r"TempImage/断言/test_case_057.png",
    #     "assert_test_case_058": r"TempImage/断言/test_case_058.png",
    #     "assert_test_case_059": r"TempImage/断言/test_case_059.png",
    #     "assert_test_case_060": r"TempImage/断言/test_case_060.png",
    #     "assert_test_case_061": r"TempImage/断言/test_case_061.png",
    #     "assert_test_case_062": r"TempImage/断言/test_case_062.png",
    #     "assert_test_case_063": r"TempImage/断言/test_case_063.png",
    #     "assert_test_case_064": r"TempImage/断言/test_case_064.png",
    #     "assert_test_case_065": r"TempImage/断言/test_case_065.png",
    #     "assert_test_case_066": r"TempImage/断言/test_case_066.png",
    #     "assert_test_case_067": r"TempImage/断言/test_case_067.png",
    #     "assert_test_case_068": r"TempImage/断言/test_case_068.png",
    #     "assert_test_case_069": r"TempImage/断言/test_case_069.png",
    #     "assert_test_case_070": r"TempImage/断言/test_case_070.png",
    #     "assert_test_case_071": r"TempImage/断言/test_case_071.png",
    #     "assert_test_case_072": r"TempImage/断言/test_case_072.png",
    #     "assert_test_case_072_1": r"TempImage/断言/test_case_072_1.png",
    #     "assert_test_case_073_1": r"TempImage/断言/test_case_073_1.png",
    #     "assert_test_case_073": r"TempImage/断言/test_case_073.png",
    #     "assert_test_case_074": r"TempImage/断言/test_case_074.png",
    #     "assert_test_case_074_1": r"TempImage/断言/test_case_074_1.png",
    #     "assert_test_case_075": r"TempImage/断言/test_case_075.png",
    #     "assert_test_case_075_1": r"TempImage/断言/test_case_075_1.png",
    #     "assert_test_case_076": r"TempImage/断言/test_case_076.png",
    #     "assert_test_case_076_1": r"TempImage/断言/test_case_076_1.png",
    #     "assert_test_case_077": r"TempImage/断言/test_case_077.png",
    #     "assert_test_case_077_1": r"TempImage/断言/test_case_077_1.png",
    #     "assert_test_case_078": r"TempImage/断言/test_case_078.png",
    #     "assert_test_case_078_1": r"TempImage/断言/test_case_078_1.png",
    #     "assert_test_case_079": r"TempImage/断言/test_case_079.png",
    #     "assert_test_case_079_1": r"TempImage/断言/test_case_079_1.png",
    # }

    IMAGE_MAP = auto_image_map()

    def __init__(self, common_instance=None):
        self.common = common_instance if common_instance else Common()

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

if __name__ == "__main__":
    print(auto_image_map())