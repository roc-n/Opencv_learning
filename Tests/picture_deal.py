from cv2 import cv2 as cv
import numpy as np


def nothing(x):
    pass


img1 = cv.imread('football.png')
img2 = cv.imread('star_.jpg')

# 输出图像信息
print(img2.shape)
print(img1.shape)
print(img2.dtype)
print(img2.size)

# 创建滑条与窗口
cv.namedWindow('transform')
cv.createTrackbar('coefficient', 'transform', 0, 100, nothing)


# 将图中足球用矩形圈出
cv.rectangle(img1, (81, 220), (134, 271), (0, 255, 0), 2)
cv.rectangle(img1, (275,230), (321,276), (0, 0, 255), 2)


while True:
    coefficients = cv.getTrackbarPos('coefficient', 'transform')

    #添加权重
    img = cv.addWeighted(img1, float(coefficients / 100.0),
                         img2, float(1.0 - (coefficients / 100.0)), 0)
    cv.imshow('transform', img)
    key = cv.waitKey(10)
    if key == 27:
        break
