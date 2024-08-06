import requests
url = 'http://192.168.21.111:48080/admin-api/infra/file/uploadWarnFile'

payload = {
    "alarm_id": "1164624018284875777",
    "device_id": "1164624018284875777",
    "preset_id": 1,
    "rule_id": 2,
    "file_type": 2,
    "channel_type": 2,
    "file": r"D:\testData\file\testFile.png",
    "file_name": "testFile.png"
}

files = {'file': open(payload['file'], 'rb')}
response = requests.post(url, data=payload, files=files)

try:
    if response.status_code == 200:
        print("请求成功")
        print(response.json())
    else:
        print("请求失败")
        print(response.text)

except Exception as e:
    print("发生异常:", e)

