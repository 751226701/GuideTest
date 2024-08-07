# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/6 19:08
# @File :run.py
# @Project : GuideTest
import sys
import demo1
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidow = QMainWindow()
    ui = untitled.Ui_Form()
    ui.setupUi(mainWidow)
    mainWidow.show()
    sys.exit(app.exec_())


