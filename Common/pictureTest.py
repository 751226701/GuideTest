import cv2
import os


def batch_test_image_sharpness(image_folder):
    image_list = [(os.path.join(image_folder, filename), 0) for filename in os.listdir(image_folder)
                  if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for i, (image_path, _) in enumerate(image_list):
        # 读取图像并转为灰度图
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # 计算清晰度得分
        sharpness_score = cv2.Laplacian(image, cv2.CV_64F).var()
        # 更新图像列表中的清晰度得分
        image_list[i] = (image_path, sharpness_score)

    # 按照清晰度得分降序排列
    image_list.sort(key=lambda x: x[1], reverse=True)

    # 重新命名照片名字
    for i, (image_path, sharpness_score) in enumerate(image_list):
        new_filename = f"{i + 1}_{sharpness_score:.2f}.jpg"
        new_path = os.path.join(image_folder, new_filename)
        os.rename(image_path, new_path)
        image_list[i] = (new_path, sharpness_score)

    return image_list


# 测试代码
if __name__ == '__main__':
    image_folder = 'D:\Testpicture'
    result = batch_test_image_sharpness(image_folder)

    # 在输出窗口竖直排列输出结果
    for item in result:
        print(item[0], item[1], '\n')

    input("Press Enter to exit...")
