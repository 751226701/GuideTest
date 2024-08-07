# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/7 11:34
# @File :demo3
# @Project : GuideTest
import sys

from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)
        self.setWindowTitle("Study")
        self.resize(400, 300)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        centerWidth = (screen.width()-size.width())/2
        centerHeight = (screen.height()-size.height())/2
        self.move(centerWidth,centerHeight)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
