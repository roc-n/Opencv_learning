from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
while(1):
    # 获取每一帧
    ret, frame = cap.read()
    # 转换到 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])


    lower_green = np.array([60, 100, 100])
    upper_green = np.array([150, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_ = cv2.inRange(hsv, lower_green, upper_green)
    
    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res_ = cv2.bitwise_and(frame, frame, mask_)
    
    # 显示图像

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    cv2.imshow('mask_', mask_)
    cv2.imshow('res_',res_)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
# 关闭窗口
cv2.destroyAllWindows()

# green = np.uint8([0, 255, 0])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# error: / builddir/build/BUILD/opencv-2.4.6.1/
# modules/imgproc/src/color.cpp: 3541:
# error: (-215)(scn == 3 | | scn == 4) & & (depth == CV_8U | | depth == CV_32F)
# in function cvtColor
# scn(the number of channels of the source),
# i.e. self.img.channels(), is neither 3 nor 4.

# depth(of the source),
# i.e. self.img.depth(), is neither CV_8U nor CV_32F.
# 所以不能用[0, 255, 0], 而要用[[[0, 255, 0]]]
# 这里的三层括号应该分别对应于 cvArray, cvMat, IplImage
# green = np.uint8([[[0, 255, 0]]])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print(hsv_green)
