import time
import paho.mqtt.client as mqtt
import uuid

def generate_device_id():
    return str(uuid.uuid4())

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnection returned result:" + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def publish_data(jsondata):
    print("publish data success>>>>>>>>>>>>>>>>>>>>>")

def on_subscribe(client, userdata, mid, granted_qos):
    print("-- on_subscribe returned mid:" + str(mid))

def publish_para():
    # clean_session=True  清除之前的消息，避免建立连接后收到之前的订阅消息
    client = mqtt.Client(client_id=generate_device_id(), clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect("192.168.21.112", 18883)
    client.loop_start()
    return client

def mqtt_on_publish_to_cloud(topic, message_dict):
    client = publish_para()
    payload = str(message_dict)
    client.publish(topic, payload)
    print(payload)
    print("mqtt向云端发送指令成功")
    time.sleep(3)


if __name__ == '__main__':
    topic = "real-time-temp"
    message_dict = {9999999999999}

    mqtt_on_publish_to_cloud(topic, message_dict)
