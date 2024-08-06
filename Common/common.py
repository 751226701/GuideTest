import base64
import os.path
import struct
import inspect
import logging
import requests
import json
import numpy as np
import datetime
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
from datetime import datetime
import xml.etree.ElementTree as ET
import ruamel.yaml as yaml

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 512
count_above = 0
count_below = 0
temp_counts = 0
MAXTEMP = 15000
MINTEMP = 0


# 530接口获取温度
def getTemp(temp):
    global count_below, count_above, temp_counts
    decode_byte_temp = base64.b64decode(temp)
    short_temp = np.frombuffer(decode_byte_temp, dtype=np.int16).astype(np.int16)
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
    print((f"异常温度概率为：{((count_above + count_below) / temp_counts / 2):.2f}"))
    print(' ')
# RSA加密
def encrpt(password):
    public_key = '''-----BEGIN PUBLIC KEY-----\n"
                      "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCsn//YAXtvUmzfcdUSVc80NgMM"
                      "NFIc/EyzOnLKcUM6Xm+up8K7AymL6TpOpgdtxDB30GlQjK7RNwJLgNSzT7d7OXJq"
                      "382cX0V6aYXA9oeZ93bsdpiDNOMNu1ezlWZNJBS2sJoUnQl7mTGJN2b44wUcqh98"
                      "F3wPTUp/+rydh3oBkQIDAQAB"
                      "\n-----END PUBLIC KEY-----'''
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    password = str(password)  # 密码为int类型时需要转化为str类型
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()
def parse_xml_report(xml_file):
    tree = ET.parse(xml_file, parser=ET.XMLParser(encoding="utf-8"))
    root = tree.getroot()
    test_cases = []

    for testsuite in root.findall('testsuite'):
        for testcase in testsuite.findall('testcase'):
            test_case_name = testcase.get('name')
            status = 'Passed'
            failure = testcase.find('failure')
            if failure is not None:
                status = 'Failed'
            test_cases.append((test_case_name, status))

    return test_cases
def generate_html_report(test_cases, html_file):
    with open(html_file, 'w') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Google Test Report</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>Google Test Report</h1>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Test Case</th><th>Status</th></tr>\n')

        for test_case, status in test_cases:
            color = 'green' if status == 'Passed' else 'red'
            f.write(f'<tr><td>{test_case}</td><td><font color="{color}">{status}</font></td></tr>\n')

        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')
def Serial_port_analysis(hex_data):
    # hex_data=hex_data.replace(" ","")

    maxTemp = int(hex_data[7:14], 16) / 100
    avgTemp = int(hex_data[15:22], 16) / 100
    minTemp = int(hex_data[23:30], 16) / 100
    alyNum = int(hex_data[31:34], 16)

    print(f"全局最高温：{maxTemp}")
    print(f"全局最低温：{minTemp}")
    print(f"全局平均温：{avgTemp}")
    print(f"分析对象个数为：{alyNum}")
    print()

    for i in range(alyNum):
        print("第%s个分析对象" % (i + 1))
        print(f"最高温：{int(hex_data[(35 + 24 * i):(42 + 24 * i)], 16) / 100}")
        print(f"最低温：{int(hex_data[(43 + 24 * i):(50 + 24 * i)], 16) / 100}")
        print(f"平均温：{int(hex_data[(51 + 24 * i):(58 + 24 * i)], 16) / 100}")
        print()
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        if isinstance(data, list):
            result = data
    return result
def getY16(url, token):
    url = "http://" + url + ":80/getmsginfo"
    data = {"action": "request",
            "cmdtype": 906,
            "message": {"value": 0},
            "sequence": 100,
            "token": token
            }
    print(url)
    res = requests.post(url=url, json=data)
    y16 = json.loads(res.text)['message']['y16']
    y16_paramLine = json.loads(res.text)['message']['y16_paramLine']
    print(y16)
    print(y16_paramLine)
    y16data = url + y16
    y16_paramLinedata = url + y16_paramLine
    urrent_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    response = requests.get(y16data)
    if response.status_code == 200:
        file_name = f"{urrent_time}_y16.raw"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"文件 {file_name} 下载成功")
    else:
        print("文件下载失败")

    response = requests.get(y16_paramLinedata)
    if response.status_code == 200:
        file_name = f"{urrent_time}_y16_paramLine.raw"
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"文件 {file_name} 下载成功")
    else:
        print("文件下载失败")
def log(message):
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger("my_logger")
    print(message)
    logger.info(message)


if __name__ == "__main__":
    xml_file = r"D:\APP\VS2022\project\Gtest\x64\Release\testreport.xml"  # 你的XML测试报告文件
    html_file = r"D:\APP\VS2022\project\Gtest\x64\Release\testreport.html"  # 输出的HTML测试报告文件

    test_cases = parse_xml_report(xml_file)
    generate_html_report(test_cases, html_file)
    print(f"HTML测试报告已生成：{html_file}")


