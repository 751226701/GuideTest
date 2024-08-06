from onvif import ONVIFCamera
import cv2


def get_onvif_stream():
    ip = '192.168.21.31'
    port = 9520
    username = 'admin'
    password = 'admin123'

    # 连接ONVIF设备
    mycam = ONVIFCamera(ip, port, username, password)

    # 创建媒体服务对象
    media_service = mycam.create_media_service()

    # 获取主流URI
    profiles = media_service.GetProfiles()
    uri = media_service.GetStreamUri({
        'StreamSetup': {
            'Stream': 'RTP-Unicast',
            'Transport': {'Protocol': 'RTSP'}
        },
        'ProfileToken': profiles[0].token
    })

    # 拉取视频流
    cap = cv2.VideoCapture(uri.Uri)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('ONVIF Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    get_onvif_stream()
