from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


tmp_img = cv.imread('star.jpg')
cnt = 0
cv.imshow('win', tmp_img)
# 向下生成三级高斯金字塔
while(True):
    cnt += 1
    print(cnt)
    tmp_img=cv.pyrDown(tmp_img)
    cv.imshow('window', tmp_img)
    key=cv.waitKey(0)
    if key == 27 and cnt == 3:
        break

cnt = 0
#向上生成三级高斯金字塔
while (True):
    cnt += 1
    print(cnt)
    tmp_img=cv.pyrUp(tmp_img)
    cv.imshow('window', tmp_img)
    key=cv.waitKey(0)
    if key == 27 and cnt == 3:
        break
cv.destroyAllWindows()
