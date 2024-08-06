"""读取RGB文件成像"""
import numpy as np
import cv2

def read_rgb_from_raw(filename, width, height):
    with open(filename, 'rb') as file:
        raw_data = file.read()

    rgb_data = np.frombuffer(raw_data, dtype=np.uint8)
    rgb_data = np.reshape(rgb_data, (height, width, 3))  #根据宽高整理数据
    return rgb_data

def main():
    width = 20
    height = 50

    filename = r"C:\Users\gd09186\Desktop\白热ColorBar.raw"
    rgb_image = read_rgb_from_raw(filename, width, height)

    cv2.imshow('RGB Image', rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
