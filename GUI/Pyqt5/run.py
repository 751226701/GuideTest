from PyQt5 import QtCore, QtGui, QtWidgets
import websocket
import json
import logging
import threading
from time import sleep
import base64
import numpy as np
from datetime import datetime
import sys

# 设置日志记录配置
logging.basicConfig(filename='output.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# 创建一个日志记录器
logger = logging.getLogger("my_logger")

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 512
count_above = 0
count_below = 0
temp_counts = 0
MAXTEMP = 99 * 100
MINTEMP = 99 * 100

class Test(object):
    def __init__(self, url, maxtemp, mintemp, width, height, dtype, output_callback):
        self.url = "ws://" + url + ":9980/api/v1/control"
        self.urls = url
        self.ws = None
        self.request = {
            "action": "request",
            "cmdtype": 501,
            "sequence": 1,
            "message": {
                "username": "admin",
                "password": "Tewp+df7dfmTQy2d5S/fmuiCXRleo26a8VYu6M0kzK1CF/UfgqMRSDiOnniU0l9nAzemdqOIt0so360nRrgM6Fun20LKGcqddentxQLpiRkKUqWQOGSPnnPxg5jb0GfKJcgymt5MhKx71vRpd/nZRFVTOkGEg6qN9+FRDrSo+hY="
            }
        }
        self.token = None
        self.temp_thread = None
        self.heart_thread = None
        self.is_running = False
        self.COUNT = 0
        self.matrix = None
        self.maxtemp = maxtemp
        self.mintemp = mintemp
        self.width = width
        self.height = height
        self.dtype = dtype
        self.output_callback = output_callback

    def on_open(self, ws):
        ws.send(json.dumps(self.request))

    def on_message(self, ws, message):
        response = json.loads(message)

        if response.get('message') and response['message'].get('token'):
            self.token = response['message']['token']
            print("Token:", self.token)

            # 开始获取温度数据
            self.start_getting_temp()
            # 启动心跳线程
            self.start_heartbeat()

        elif self.token and response.get('cmdtype') and response['cmdtype'] == 530:
            if response['retcode'] == 10021:
                print('pass')
            else:
                temp = response['message']['temps']
                self.getTemp(temp)

    def on_error(self, ws, error):
        print("Error:\n")
        print(f"连接失败:{error}")

    def on_close(self, ws, close_status_code, close_msg):
        self.ws.close()
        print("WebSocket connection closed")

    def start_connect(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()

    def start_getting_temp(self):
        self.is_running = True
        self.temp_thread = threading.Thread(target=self._get_temp_thread)
        self.temp_thread.start()

    def start_heartbeat(self):
        self.is_running = True
        self.heart_thread = threading.Thread(target=self._heartbeat_thread)
        self.heart_thread.start()

    def _heartbeat_thread(self):
        while self.is_running:
            if self.token:
                # 发送心跳
                re = {
                    "action": "request",
                    "cmdtype": 9999,
                    "message": {},
                    "sequence": 1,
                    "token": self.token
                }
                self.ws.send(json.dumps(re))
            sleep(30)

    def _get_temp_thread(self):
        while self.is_running:
            if self.token:
                # 发送获取温度的请求
                request_03 = {
                    "action": "request",
                    "cmdtype": 530,
                    "sequence": 1,
                    "token": self.token,
                    "message": {
                        "type": 0
                    }
                }
                self.ws.send(json.dumps(request_03))

            sleep(1)

    def stop_connect(self):
        self.is_running = False
        self.ws.close()

    def getTemp(self, temp):
        global count_below, count_above, temp_counts
        decode_byte_temp = base64.b64decode(temp)
        short_temp = np.frombuffer(decode_byte_temp, dtype=self.dtype).astype(self.dtype)
        maxtemp = short_temp[0]
        mintemp = short_temp[0]

        for i in range(min(len(short_temp), self.width * self.height)):
            if maxtemp <= short_temp[i]:
                maxtemp = short_temp[i]
            if mintemp >= short_temp[i]:
                mintemp = short_temp[i]

        if maxtemp > self.maxtemp or mintemp > self.maxtemp:
            count_above += 1
        if maxtemp < self.mintemp or mintemp < self.mintemp:
            count_below += 1
        temp_counts += 1
        current_time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        output_text = (f"获取的温度次数:{temp_counts}\n"
                       f"{current_time} maxTemp: {maxtemp / 100}\n"
                       f"{current_time} minTemp: {mintemp / 100}\n"
                       f"{current_time} 高于{self.maxtemp / 100}的温度次数：{count_above}\n"
                       f"{current_time} 低于{self.mintemp / 100}的温度次数：{count_below}\n\n")

        self.output_callback(output_text)

        logger.info(output_text)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("int16")
        self.comboBox.addItem("int32")
        self.comboBox.setCurrentText("int32")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 6, 0, 1, 2)

        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 7, 0, 1, 2)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 8, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_start.clicked.connect(self.start_test)
        self.pushButton_stop.clicked.connect(self.stop_test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GetTemp"))
        self.label_1.setText(_translate("MainWindow", "设备IP地址："))
        self.label_2.setText(_translate("MainWindow", "高温阈值："))
        self.label_3.setText(_translate("MainWindow", "低温阈值："))
        self.label_4.setText(_translate("MainWindow", "图像宽度："))
        self.label_5.setText(_translate("MainWindow", "图像高度："))
        self.label_6.setText(_translate("MainWindow", "数据类型："))
        self.pushButton_start.setText(_translate("MainWindow", "开始测试"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止测试"))

    def start_test(self):
        url = self.lineEdit_1.text()
        maxtemp = int(self.lineEdit_2.text()) * 100
        mintemp = int(self.lineEdit_3.text()) * 100
        width = int(self.lineEdit_4.text())
        height = int(self.lineEdit_5.text())
        dtype = np.int16 if self.comboBox.currentText() == 'int16' else np.int32

        self.test = Test(url, maxtemp, mintemp, width, height, dtype, self.update_output)
        self.test_thread = threading.Thread(target=self.test.start_connect)
        self.test_thread.start()

    def stop_test(self):
        if hasattr(self, 'test'):
            self.test.stop_connect()

    def update_output(self, text):
        self.textEdit.append(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
