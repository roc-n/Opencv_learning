from cv2 import cv2 as cv
import numpy as np


# 滑块回调函数
def nothing(x):
    pass


# 创建底板
img = np.zeros((600, 1000, 3), np.uint8)
img[:] = [255, 255, 255]
# 创建窗口与滑条
cv.namedWindow('images')
cv.createTrackbar('R', 'images', 0, 255, nothing)
cv.createTrackbar('G', 'images', 0, 255, nothing)
cv.createTrackbar('B', 'images', 0, 255, nothing)


# 第二次按下标志
drawing = False
# 箭头坐标
x_, y_ = -1, -1


# 绘制图形的回调函数
def draw(event, x, y, flags, param):
    global x_, y_, drawing  # 声明变量为global以进行更改
    # 左键双击以绘制圆形
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, colors, -1)
    # 先后按下中键以绘制矩形
    elif event == cv.EVENT_MBUTTONDOWN and drawing == False:
        cv.circle(img, (x, y), 3, colors, -1)
        x_, y_ = x, y
        drawing = True
    elif event == cv.EVENT_MBUTTONDOWN and drawing == True:
        cv.rectangle(img, (x_, y_), (x, y), colors, -1)
        drawing = False


# 将鼠标回调函数与图片关联
cv.setMouseCallback('images', draw)
while True:
    cv.imshow('images', img)
    k = cv.waitKey(20)
    if k == 27:
        break
    # 设置颜色
    r = cv.getTrackbarPos('R', 'images')
    g = cv.getTrackbarPos('G', 'images')
    b = cv.getTrackbarPos('B', 'images')
    colors = [r, g, b]

cv.destroyWindow("Trackbar image")
