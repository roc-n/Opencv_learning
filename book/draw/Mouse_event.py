from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


# 鼠标按下时变为True
drawing = False
# 如果mode为True绘制矩形,按'm'绘制曲线
mode = True
ix, iy = -1, -1

img = np.zeros((512, 512, 3), np.uint8)

# 创建回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
# 按下左键返回起始坐标位置坐标
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

# 鼠标左键按下并移动绘制图形,event查看移动,flag查看是否按下
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
            else:
                # 绘制圆圈
                cv.circle(img, (x, y), 3, (0, 0, 255), -1)

# 鼠标松开停止绘画
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
