from cv2 import cv2 as cv
import numpy as np
import time
img = cv.imread("star.jpg")
e1 = cv.getTickCount()  # 也可用python的time模块计数


# 估量代码执行效率
for i in range(5, 49, 2):
    img = cv.medianBlur(img, i)
e2 = cv.getTickCount()
time = (e2 - e1) / cv.getTickFrequency()
print(time)


# 查看是否开启优化
ret = cv.useOptimized()
print(ret)

# 魔法命令%time（使用ipython）
