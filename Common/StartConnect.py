import websocket
import json
from Files import Test_File as R
from common import getTemp, encrpt
import threading
import datetime
from datetime import datetime
from time import sleep

class Test(object):
    def __init__(self, request):
        self.url = "ws://192.168.21.53:9980/api/v1/control"
        self.ws = None
        self.request = request
        self.token = None
        self.temp_thread = None
        self.heart_thread = None
        self.is_running = False
        self.ShutterCount=0

    def on_open(self, ws):
        ws.send(json.dumps(self.request))

    def on_message(self, ws, message):
        response = json.loads(message)
        # print(response)

        if response.get('message') and response['message'].get('token'):
            self.token = response['message']['token']
            print("Token:", self.token)

            # 开始获取温度数据
            self.start_getting_temp()
            # 启动心跳线程
            self.start_heartbeat()

        elif self.token and response.get('cmdtype') and response['cmdtype']==530:
            if response['retcode']==10021:
                self.ShutterCount+=1
                print('打快门！')
            else:
                temp = response['message']['temps']
                getTemp(temp)
                # time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                # print(f"{time}打快门次数：{self.ShutterCount}")

    def on_error(self, ws, error):
        print("Error:\n")
        print(error)
        print("连接失败")

    def on_close(self, ws):
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

            sleep(0.5)

    def stop_connect(self):
        self.is_running = False
        self.ws.close()


if __name__ == "__main__":
   test = Test(R.request_02)
   test.start_connect()







