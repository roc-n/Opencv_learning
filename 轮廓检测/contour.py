from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


# 绘制轮廓准备工作,二值图像准确率更高
img = cv.imread('contour.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# 新版opencv findContours只返回两个参数
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


# 绘制轮廓
draw_img = img.copy()
res = cv.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
# cv_show('res', res)

# 一些轮廓函数
cnt = contours[0]
area = cv.contourArea(cnt)
print(area)
length = cv.arcLength(cnt, True)
print(round(length, 3))

# 轮廓近似
epsilon = 0.01 * length
approx = cv.approxPolyDP(cnt, epsilon, True)
draw_img = img.copy()
res = cv.drawContours(draw_img, [approx], -1, (255, 0, 0), 2)
# cv_show('res', res)

# 针对轮廓的一些ui操作
x, y, w, h = cv.boundingRect(cnt)
img1 = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 外接矩形
cv_show('img1', img1)
rect_area = w * h
extent = float(area) / rect_area

(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img2 = cv.circle(img, center, radius, (0, 255, 0), 2)
cv_show('img2', img2)
