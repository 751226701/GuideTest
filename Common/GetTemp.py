import websocket
import json
import logging
import threading
from time import sleep
import base64
import numpy as np
import datetime
from datetime import datetime
import requests
import time
import cv2

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
url = input("请输入设备IP地址：")
maxtemp = input("请输入高温记录阈值：")
mintemp = input("请输入低温记录阈值：")
MAXTEMP = int(maxtemp) * 100
MINTEMP = int(mintemp) * 100

def getMatrix(temp):
    decode_byte_temp = base64.b64decode(temp)
    short_temp = np.frombuffer(decode_byte_temp, dtype=np.int16).astype(np.int16)
    return short_temp
def getTemp(temp):
    global count_below, count_above, temp_counts, mintemp
    decode_byte_temp = base64.b64decode(temp)

    short_temp = np.frombuffer(decode_byte_temp, dtype=np.int32).astype(np.int32)
    maxtemp = short_temp[0]
    mintemp = short_temp[0]

    for i in range(min(len(short_temp), IMAGE_WIDTH * IMAGE_HEIGHT)):
        # print(short_temp[i])
        if maxtemp <= short_temp[i]:
            maxtemp = short_temp[i]
        if mintemp >= short_temp[i]:
            mintemp = short_temp[i]

    if maxtemp > MAXTEMP or mintemp > MAXTEMP:
        count_above += 1
    if maxtemp < MINTEMP or mintemp < MINTEMP:
        count_below += 1
    temp_counts += 1
    time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    print(f"获取的温度次数:{temp_counts}")
    print(f"{time}maxTemp: {maxtemp / 100}")
    print(f"{time}minTemp: {mintemp / 100}")
    print(f"{time}高于{MAXTEMP / 100}的温度次数：{count_above}")
    print(f"{time}低于{MINTEMP / 100}的温度次数：{count_below}")
    # print((f"异常温度概率为：{((count_above+count_below)/temp_counts/2):.2f}"))
    print(' ')

    # # 使用日志记录器记录日志信息
    logger.info(f"{time}获取的温度次数:{temp_counts}")
    logger.info(f"{time}maxTemp: {maxtemp / 100}")
    logger.info(f"{time}minTemp: {mintemp / 100}")
    logger.info(f"{time}高于{MAXTEMP / 100}的温度次数：{count_above}")
    logger.info(f"{time}低于{MINTEMP / 100}的温度次数：{count_below}")
    logger.info(' ')
def getY16(url, token):
    urls = url
    url = "http://" + url + ":80/getmsginfo"
    data = {"action": "request",
            "cmdtype": 906,
            "message": {"value": 0},
            "sequence": 100,
            "token": token
            }
    res = requests.post(url=url, json=data)
    y16 = json.loads(res.text)['message']['y16']
    y16_paramLine = json.loads(res.text)['message']['y16_paramLine']
    y16data = "http://" + urls + y16
    y16_paramLinedata = "http://" + urls + y16_paramLine
    global current_time
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    response = requests.get(y16data)
    start_time = time.time()
    if response.status_code == 200:
        file_name = f"{current_time}_y16.raw"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"文件 {file_name} 下载成功")
    else:
        print("文件下载失败")

    response = requests.get(y16_paramLinedata)
    if response.status_code == 200:
        file_name = f"{current_time}_y16_paramLine.raw"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"文件 {file_name} 下载成功")
    else:
        print("文件下载失败")
    end_time = time.time()
    download_time = end_time - start_time
    # print(f"下载耗时 {download_time:.2f} 秒")
def saveTemps(temp):
    global count_below, count_above, temp_counts, mintemp
    decode_byte_temp = base64.b64decode(temp)
    count = len(decode_byte_temp) // 4

    short_temp = np.frombuffer(decode_byte_temp, dtype=np.int32).astype(np.int32)
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'{current_time}TempData.txt'

    with open(filename, 'wb') as file:
        for value in short_temp:
            file.write(str(value).encode() + b'\r\n')

    # with open(filename, 'w') as file:
    #     for i in range(512):
    #         row_values = short_temp[i * 640:(i + 1) * 640]
    #         row_string = " ".join(map(str, row_values))
    #         file.write(row_string + "\n")



class Test(object):
    def __init__(self):
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
            # self.start_other_thread()

        elif self.token and response.get('cmdtype') and response['cmdtype'] == 530:
            if response['retcode'] == 10021:
                print('pass')
            else:
                temp = response['message']['temps']
                getTemp(temp)
                self.matrix = getMatrix(temp)
                # if (int(mintemp)/100)<-40:
                #     getY16(url=self.urls,token=self.token)
                #     saveTemps(temp)
                #     self.COUNT+=1
                #     if self.COUNT>2000:
                #         self.stop_connect()

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

    def start_other_thread(self):
        threading.Thread(target=self._other_thread).start()

    def start_getting_temp(self):
        self.is_running = True
        self.temp_thread = threading.Thread(target=self._get_temp_thread)
        self.temp_thread.start()

    def start_heartbeat(self):
        self.is_running = True
        self.heart_thread = threading.Thread(target=self._heartbeat_thread)
        self.heart_thread.start()

    def _other_thread(self):
        pass

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


if __name__ == "__main__":
    Test().start_connect()


