from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()

def nothing(x):
    pass

cv.namedWindow('win', cv.WINDOW_NORMAL)
# 创建滑动条
bar = cv.createTrackbar('equ', 'win', 0, 10, nothing)
img = cv.imread('image/hist.jpg', 0)

while True:
    x = cv.getTrackbarPos('equ', 'win')
    # 进行均衡化
    clahe = cv.createCLAHE(clipLimit=x, tileGridSize=(8, 8))
    cl = clahe.apply(img)
    cv.imshow('win', cl)
    key = cv.waitKey(10)
    if (key == 27):
        break

# 2D直方图展示
img = cv.imread('image/hist.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [150, 256], [0, 180, 0, 256])
plt.imshow(hist, interpolation='nearest')
plt.show()
