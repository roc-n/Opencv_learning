from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


# 绘制轮廓准备工作,二值图像准确率更高,也可以用Canny边缘检测
img = cv.imread('contour.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,127,255, cv.THRESH_BINARY)

# 新版opencv findContours只返回两个参数
ret, contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
draw_img = img.copy()  # 创建副本
res = cv.drawContours(draw_img, contours, -1, (255,0,0), 1)
cv_show('res', res)



