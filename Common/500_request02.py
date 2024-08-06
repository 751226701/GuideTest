import requests
import time
from time import sleep
from datetime import datetime
import sys


def send_http_request(url, payload):
    try:
        start_time = time.time()
        response = requests.post(url, json=payload, timeout=2)
        end_time = time.time()

        if response.status_code == 200:
            print("请求成功!")
            # print("请求成功，响应时间：", response.json()["message"]["datetime"])
        else:
            print("请求失败，状态码：", response.status_code)

        response_time = end_time - start_time
        # print("响应时间：{:.2f}秒".format(response_time))

    except requests.Timeout:
        print("请求超时！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    COUNT = 1
    # sys.stdout = open("console_output.log", "a")
    url = "http://192.168.21.152:80/getmsginfo"
    payload = {
        "action": "request",
        "cmdtype": 500,
        "sequence": 1,
        "message": {}
    }

    while True:
        CYCLE_TIME = 40
        print(f"第{COUNT}次上电！")
        COUNT += 1
        request_time = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        print(f"请求发送时间{request_time}")
        start_time = time.time()
        send_http_request(url, payload)
        end_time = time.time()
        response_time = end_time - start_time
        print("响应时间：{:.2f}秒".format(response_time))
        wait_time = max(CYCLE_TIME - response_time, 0)
        print()
        sleep(wait_time)
