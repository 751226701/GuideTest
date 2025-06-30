#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/25
# @file: test_case_add_component.py
# @project: EAI 2.0 GUI_TEST

import os
import time
import pytest
from Config.Config import Config
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Pages.Engineer import Engineer
yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
eng = Engineer()

@pytest.mark.usefixtures("gui_app")
class TestAddComponent:

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self,CaseData:dict):
        """
        自动化添加地轨 + 机器人 + 工具
        """
        # 添加地轨
        eng.click_new()
        eng.click_additional_axis()
        eng.click_ground_track()
        eng.click_welding_ground_track()
        eng.click_confirm()
        eng.assert_welding_ground_track()

        # 添加机器人
        eng.click_robot()
        eng.click_robot_IRB14140()
        eng.click_world_dropdown()
        eng.click_BoZhongWeldRail()
        eng.click_confirm()
        eng.assert_robot_IRB14140()

        # 添加工具
        eng.click_tool()
        eng.click_tool_HQ2()
        time.sleep(1)
        eng.click_world_dropdown()
        eng.click_IRB1410()
        eng.click_confirm()
        eng.assert_tool_HQ2()

    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, CaseData: dict):
        """
        自动化添加地轨 + 机器人 + 工具
        """
        # 添加地轨
        eng.click_additional_axis()
        eng.click_ground_track()
        eng.click_welding_ground_track()

