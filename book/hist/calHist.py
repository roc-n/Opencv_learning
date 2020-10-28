"""
calHist与histogram函数
"""

from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('star.jpg')
# image：原图像，传入时[]括起来
# channels,灰度图用[0]括起来，彩色图像[0],[1],[2]括起来
# mask 整幅图为None,局部需传入掩模
# BIN的数目，[]括起来
# ranges 像素值范围
hist = cv.calcHist([img], [0], None, [256], [0, 256])

# bins= np.histogram(img.ravel(), 256, [0, 256]);

# 绘直方图
# 简单方法-matplotlib  复杂函数-Opencv
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
color = ('b', 'g', 'r')

# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置 enumerrate 函数会有更加直接,优美的做法
# enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()


# 局部函数
img = cv.imread('tree.jpg', 0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)

mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
# Calculate histogram with mask and without mask
# Check third argument for masks
hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()
