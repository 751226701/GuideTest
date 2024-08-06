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
    message = msg.payload.decode("UTF-8")
    print("Received message: " + message)

def on_subscribe(client, userdata, mid, granted_qos):
    print("on_subscribe returned mid:" + str(mid))

def on_unsubscribe(client, userdata, mid, granted_qos):
    print("On unSubscribed: qos = %d" % granted_qos)

def mqtt_on_subscribe(topic):
    client = mqtt.Client(client_id=generate_device_id(), clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.connect("192.168.21.3", 1883)
    client.loop_start()  # 开启一个单线程
    client.subscribe(topic,qos=1)

    while True:
        print("mqtt指令监听中......")
        time.sleep(2)

if __name__ == '__main__':
    topic = "real-time--change"

    mqtt_on_subscribe(topic)

