from os import name
from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
""""腐蚀与膨胀操作均针对白色部分"""


def cv_imshow(img, name):
    cv.imshow(name, img)
    key = cv.waitKey(0)
    if key == 27:
        cv.destroyAllWindows()


img = cv.imread('timg.jpg', 0)
kernel = np.ones((2, 3), np.uint8)  # 核（结构元素，可以为矩形，椭圆，十字形）
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# kernel = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))

# 腐蚀操作即在原图象的小区域内取局部最小值,
erosion = cv.erode(img, kernel, iterations=5)
# 膨胀取局部最大值.
dilation = cv.dilate(img, kernel, iterations=5)
# cv_imshow(dilation, 'dialation')

# 开闭运算.开运算：erode->dialate
# 闭运算：dialate->erode(先膨胀会使白色的部分扩张，
# 以至于消除"闭合"物体里面的小黑洞，所以叫闭运算)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv_imshow(opening, 'opening')
cv_imshow(closing, 'closing')


# 形态学梯度运算:膨胀-腐蚀得到轮廓
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# 🎩与黑帽
# 🎩:原始输入-开运算
# 黑帽:闭运算-原始输入
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


# erosion3 = cv.dilate(erosion1, kernel, iterations=1)
# res = np.vstack((erosion, erosion1, erosion3))
# cv.imshow('res', blackhat)
# cv.waitKey(0)
# cv.destroyAllWindows()
