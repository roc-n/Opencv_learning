import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 回调函数
def control(x):
    pass


# img = np.zeros((300, 512, 3), np.uint8)
# cv.namedWindow('image')
# cv.createTrackbar('R', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0, 255, nothing)
# cv.createTrackbar('B', 'image', 0, 255, nothing)

# while (True):
#     cv.imshow('image', img)
#     if cv.waitKey(1) == 27:
#         break


# # 获取滑块的值
# r = cv.getTrackbarPos('R', 'image')
# g = cv.getTrackbarPos('G', 'image')
# b = cv.getTrackbarPos('B', 'image')
# img[:]=[b,g,r]
cv.createTrackbar('button','vedio',0,255,)
