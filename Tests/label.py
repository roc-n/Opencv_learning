from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# 显示图像函数


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()

img = cv.imread('image/label.jpg')

# 第一步,将蓝色边框及字体转变为黑色
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# 获取蓝色阈值
lower_blue = np.array([90, 43, 46])
upper_blue = np.array([110, 255, 255])
mask = cv.inRange(hsv, lower_blue, upper_blue)
# 获取仅存蓝色边框及字体的图像
res = cv.bitwise_and(img, img, mask=mask)
gray_img = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# 像素值转换
for x in range(gray_img.shape[0]):
    for y in range(gray_img.shape[1]):
        px = gray_img.item(x, y)
        if(px != 0):
            img[x][y][2] = 0  # 这里选择3通道,因为显示效果最好
# 转化为灰度图以进行阈值操作
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, th = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv_show('img', th)
