import datetime

def reSetName(file_name):
    file_parts = file_name.split('_')
    prefix = '_'.join(file_parts[:-2])  # 获取时间戳之前的部分
    suffix = file_parts[-1]  # 获取时间戳之后的部分

    timestamp_part = file_parts[-2]  # 获取时间戳部分
    timestamp = int(timestamp_part) / 1000  # 将毫秒时间戳转换为秒

    # 将时间戳转换为日期时间对象
    date_time = datetime.datetime.fromtimestamp(timestamp)
    new_file_name = f"{prefix}_{date_time.strftime('%Y%m%d%H%M%S')}_{suffix}"
    return new_file_name

file_name = "IR_1184498221234393089_1702906512000_2.zip"
print(reSetName(file_name))




