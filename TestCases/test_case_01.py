#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: 刘涛
# @time: 2025/6/25
# @file: test_case_add_component.py
# @project: EAI 2.0 GUI_TEST
import os
import pytest
from Config.Config import Config
from Common.ReadYaml import ReadYaml
from Common.AllurePretty import PrettyAllure
from Pages.Engineer import Engineer
from Common.Common import Common

yaml_data = ReadYaml(os.path.join(Config.test_datas_dir, "test_data_01.yaml")).read(slice(73,79))
com = Common()
eng = Engineer(common_instance=com)


@pytest.mark.usefixtures("gui_app")
class TestAddComponent:
    
    @PrettyAllure.PrettyAllureWrapper
    @pytest.mark.parametrize("CaseData", yaml_data)
    def test_case_01(self, CaseData: dict):
        # 关键字驱动执行
        steps = CaseData.get("步骤")
        if steps:
          com.run_steps(steps, eng, com)
        else:
          pytest.skip("无步骤，跳过")






