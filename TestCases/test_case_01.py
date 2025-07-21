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
from Common.Common import Common
yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml"))
eng = Engineer()
com = Common()

@pytest.mark.usefixtures("gui_app")
class TestAddComponent:
    """
    机器人导入测试
    """

    """进入机器人页面"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_01"]))
    def test_case_01(self,CaseData:dict):
        eng.click_new()
        eng.click_gc()
        eng.click_gc_rob()
        com.assert_exists(CaseData["断言图片"])

    """导入ABB机器人IRB1200_5到世界坐标系"""
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data.read(["test_case_02"]))
    def test_case_02(self, CaseData: dict):
        pass





