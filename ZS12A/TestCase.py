import json
import requests
url = 'http://192.168.21.67:8082/iptserver/wlg/deviceList'

payload = {
    "device_id": "",
    "page_no":"1",
    "page_size":"2"
}

response = requests.post(url=url, json=payload)

try:
    if response.status_code==200:
        print("请求成功！")
        print(response.json())
    else:
        print("请求失败")
        print(response.text)

except Exception as e:
    print("发生异常:", e)

