from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔
# (尺寸变小,分辨率降低)。
img = cv.imread('star.jpg')
cv.imshow('img',img)
lower_reso = cv.pyrDown(img)
high_reso=cv.pyrUp(lower_reso)
cv.imshow('lower_case', lower_reso)
cv.imshow('high_reso',high_reso)
key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
