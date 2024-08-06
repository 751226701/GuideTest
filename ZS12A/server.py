from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)  # 实例化一个flask对象
app.debug = True
logging.basicConfig(filename='requests.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/admin-api/infra/file/uploadWarnFile', methods=['POST'])
def upload_warn_file():
    if request.method == 'POST':
        alarm_id = request.form.get('alarm_id')
        device_id = request.form.get('device_id')
        file_name = request.form.get('file_name')

        log_msg = (f"Received POST request\n - Path: {request.path}\n "
                   f"- Method: {request.method}\n - Data: {request.form}")
        logging.info(log_msg)

        if 'file' not in request.files:
            return jsonify({"code": 1, "data": False, "msg": "No file uploaded"})

        uploaded_file = request.files['file']
        if uploaded_file:
            base_path = r'D:\testData\Save'  # 保存文件的基础路径
            sub_directory = ''
            if request.form.get('channel_type') == '1':
                sub_directory = 'VL_picture' if request.form.get('file_type') == '1' else 'VL_video'
            elif request.form.get('channel_type') == '2':
                sub_directory = 'IR_picture' if request.form.get('file_type') == '1' else 'IR_video'

            save_path = os.path.join(base_path, sub_directory)
            if not os.path.exists(save_path):  # 确认路径是否存在，不存在创建
                os.makedirs(save_path)
            uploaded_file.save(os.path.join(save_path, file_name))
            return jsonify({"retcode": 0, "data": True, "retmsg": {'alarm_id': alarm_id, 'device_id': device_id}})

        return jsonify({"code": 1, "data": False, "msg": "Unexpected error occurred"})


if __name__ == '__main__':
    ip = input("请输入服务器IP：")
    app.run(host=ip, port=48080, use_reloader=False)  # 配置服务器IP、端口，启动服务

