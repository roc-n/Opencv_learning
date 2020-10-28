from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('image/front.jpg')

ori = cv.cvtColor(img, cv.COLOR_BGR2RGB)
x_, y_ = 99, 34
x__, y__ = 405, 311
mask = np.zeros(img.shape[:2], np.uint8)
# 前后景模型
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (x_, y_, x__, y__)
# 获取第一个mask
mask, bgdModel, fgdModel = cv.grabCut(
    img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)


plt.subplot(141), plt.imshow(mask), plt.xticks([]), plt.yticks([])


# 一开始以为交互程序是要自己画矩形

# drawing = False
# cv.namedWindow('win')
# def draw(event, x, y, flags, param):
#     global x_, y_, drawing, rect, x__, y__
#     if event == cv.EVENT_LBUTTONDOWN and drawing == False:
#         cv.circle(img, (x, y), 3, (0, 0, 255), 4)
#         x_, y_ = x, y
#         drawing = True
#     elif event == cv.EVENT_LBUTTONDOWN and drawing == True:
#         cv.rectangle(img, (x_, y_), (x, y), (0, 0, 255), 4)
#         drawing = False
#         x__, y__ = x, y

# cv.setMouseCallback('win', draw)
# while True:
#     cv.imshow('win', img)
#     k = cv.waitKey(20)
#     if k == 27:
#         break

# 读取修改后的图像作为修改的凭据
newMask = cv.imread('image/mask_last4.png', 0)
mask[newMask == 0] = 0
mask[newMask == 255] = 1
plt.subplot(142), plt.imshow(mask)

# 获取更新后的mask
mask, bgdModel, fgdModel = cv.grabCut(
    img, mask, None, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_MASK)
plt.subplot(143), plt.imshow(mask)

mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask[:, :, np.newaxis]
# 最后转化成matplotlib的RGB模式
res = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imwrite('image/copy.jpg', img)
plt.subplot(144), plt.imshow(img)
plt.show()
