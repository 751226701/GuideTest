# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author : 刘涛
# @Time : 2024/8/1 13:21
# @File :GUI02
# @Project : GuideTest
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QComboBox, QPushButton, QTextEdit, QLabel)

class ApiTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.response_text = None
        self.send_button = None
        self.method_combo = None
        self.body_input = None
        self.url_input = None
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('APITEST')
        self.resize(300, 400)

        # 创建布局
        layout = QVBoxLayout()

        # 创建URL输入框
        self.url_input = QLineEdit(self)
        layout.addWidget(QLabel('URL:'))
        layout.addWidget(self.url_input)

        # 创建请求体输入框
        self.body_input = QLineEdit(self)
        layout.addWidget(QLabel('Request Body:'))
        layout.addWidget(self.body_input)

        # 创建请求方法下拉选择框
        self.method_combo = QComboBox(self)
        self.method_combo.addItem('POST')
        self.method_combo.addItem('GET')
        layout.addWidget(QLabel('Method:'))
        layout.addWidget(self.method_combo)

        # 创建发送按钮
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_request)
        layout.addWidget(self.send_button)

        # 创建显示响应的文本区域
        self.response_text = QTextEdit(self)
        self.response_text.setReadOnly(True)
        layout.addWidget(QLabel('Response:'))
        layout.addWidget(self.response_text)

        # 设置布局
        self.setLayout(layout)

    def send_request(self):
        global response
        url = self.url_input.text()
        body = self.body_input.text()
        method = self.method_combo.currentText()

        # 根据请求方法发送请求
        if method == 'POST':
            import json
            try:
                body_data = json.loads(body)
                response = requests.post(url, json=body_data)
            except json.JSONDecodeError:
                self.response_text.setText('Invalid JSON format for request body.')
                return
        elif method == 'GET':
            response = requests.get(url)

        # 显示响应
        self.response_text.setText(response.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ApiTestApp()
    ex.show()
    sys.exit(app.exec_())

