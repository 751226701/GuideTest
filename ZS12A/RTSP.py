import cv2
rtsp_url = "rtsp://[fc00:614:0:4500:0:1:1:116]:554/cam/realmonitor?channel=1&subtype=0"
cap = cv2.VideoCapture(rtsp_url)

desired_width = 640
desired_height = 512

cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

if not cap.isOpened():
    print("无法连接到视频流")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (desired_width, desired_height))

    cv2.imshow('RTSP Stream', resized_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
