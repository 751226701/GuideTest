import numpy as np
import cv2


def read_raw_table(filename):
    with open(filename, 'rb') as file:
        data = np.fromfile(file, dtype=np.uint8)

    # 分离颜色通道
    B = data[0::4]  # 蓝色通道
    G = data[1::4]  # 绿色通道
    R = data[2::4]  # 红色通道

    return R, G, B


def main():
    # 读取颜色数据
    R, G, B = read_raw_table(r"C:\Users\gd09186\Desktop\LinuxTestData\冰火Color.raw")

    # 将颜色通道数据整理成图像格式
    wid = 3
    hei = 256
    pSrc3 = np.zeros((hei, wid), dtype=np.uint8)
    pSrc3[:, 0] = R
    pSrc3[:, 1] = G
    pSrc3[:, 2] = B

    pSrc5 = np.zeros((256, 20, 3), dtype=np.uint8)
    for i in range(256):
        for j in range(20):
            pSrc5[i, j, :] = pSrc3[255 - i, :]

    # 显示图像
    cv2.imshow('ColorBar_Image', pSrc5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('ColorBar_image.png', pSrc5)   #保存为文件


if __name__ == "__main__":
    main()
