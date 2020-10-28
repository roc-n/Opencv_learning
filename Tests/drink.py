from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


def nothing(x):
    pass


img = cv.imread('image/drink.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 153, 28])
upper = np.array([80, 232, 197])
mask = cv.inRange(hsv, lower, upper)
res = cv.bitwise_and(img, img, mask=mask)
cv_show('res', res)

# # 通过滑动条获取正确的上下阈值。
# cv.namedWindow('window',cv.WINDOW_NORMAL)
# cv.createTrackbar('low_1', 'window', 0, 255, nothing)
# cv.createTrackbar('low_2', 'window', 0, 255, nothing)
# cv.createTrackbar('low_3', 'window', 0, 255, nothing)
# cv.createTrackbar('up_1', 'window', 0, 255, nothing)
# cv.createTrackbar('up_2', 'window', 0, 255, nothing)
# cv.createTrackbar('up_3', 'window', 0, 255, nothing)
# while (True):
#     low_1 = cv.getTrackbarPos('low_1', 'window')
#     up_1 = cv.getTrackbarPos('up_1', 'window')
#     low_2 = cv.getTrackbarPos('low_2', 'window')
#     up_2 = cv.getTrackbarPos('up_2', 'window')
#     low_3 = cv.getTrackbarPos('low_3', 'window')
#     up_3 = cv.getTrackbarPos('up_3', 'window')
#     lower = np.array([low_1, low_2, low_3])
#     upper = np.array([up_1, up_2, up_3])
#     mask = cv.inRange(hsv, lower, upper)
#     res = cv.bitwise_and(img, img, mask=mask)

#     cv.imshow('window', res)
#     key = cv.waitKey(10)
#     if key == 27:
#         break


# 获取灰度图
gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# cv_show('gray', gray)
# 自适应阈值图
ret, res = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# cv_show('res', res)
# 寻找轮廓
ret, contours, hie = cv.findContours(
    res, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 排序轮廓
cnts = sorted(contours, key=cv.contourArea, reverse=True)[:5]
cnt = cnts[0]

# 获取矩形参数
x, y, w, h = cv.boundingRect(cnt)
# 绘制矩形
img1 = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# 获取最小外切圆
(x, y), radius = cv.minEnclosingCircle(cnt)
# 绘制圆形
img2 = cv.circle(img, (int(x), int(y)), int(radius), (0, 255, 0), 2)

cv_show('img', img)
cv.imwrite('result.jpg',img)
print("矩形中心点：")
print((float((x + w) / 2), float(y + h) / 2))
print("\n圆形圆心：")
print((x, y))

# 矩形四个极点
leftTop = tuple(cnt[cnt[:, :, 0].argmin()][0])
righTop = tuple(cnt[cnt[:, :, 0].argmax()][0])
upTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
downTop = tuple(cnt[cnt[:,:, 1].argmax()][0])
rec = [leftTop, righTop, upTop, downTop]
print('四个极点:')
for i in range(4):
    print(rec[i])
