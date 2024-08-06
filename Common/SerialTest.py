import serial
from Common.common import log


def Serial_port_analysis(hex_data):
    # hex_data=hex_data.replace(" ","")

    maxTemp = int(hex_data[7:14], 16) / 100
    minTemp = int(hex_data[15:22], 16) / 100
    avgTemp = int(hex_data[23:30], 16) / 100
    alyNum = int(hex_data[31:34], 16)

    log(f"全局最高温：{maxTemp}")
    log(f"全局最低温：{minTemp}")
    log(f"全局平均温：{avgTemp}")
    log(f"分析对象个数为：{alyNum}")
    log(" ")

    for i in range(alyNum):
        log("第%s个分析对象" % (i + 1))
        log(f"最高温：{int(hex_data[(35 + 24 * i):(42 + 24 * i)], 16) / 100}")
        log(f"最低温：{int(hex_data[(43 + 24 * i):(50 + 24 * i)], 16) / 100}")
        log(f"平均温：{int(hex_data[(51 + 24 * i):(58 + 24 * i)], 16) / 100}")
        log(" ")


ser = serial.Serial("COM11", 9600)
try:
    if not ser.is_open:
        ser.open()
    if ser.is_open:
        command = '05 03 00 00 00 7F 05 AE'
        command = bytes.fromhex(command)  # 只能接受16进制字节串
        ser.write(command)

        response = ser.read(223)
        # print(f'Response: {response.hex()}')    #转化为16进制字符串打印
        Serial_port_analysis(response.hex())  # 分析对象解析，仅用于解析分析对象
        # log(response.hex())
    else:
        print("Failed to open the serial port.")
except serial.SerialException as E:
    log(E)
    print(E)
finally:
    ser.close()


# 05 03 00 00 00 7F 05 AE  获取全局和分析对象温度
# 05 06 00 00 00 7F C9 AE  保存热图到FTP服务器


