import numpy as np
from cv2 import cv2 as cv
from matplotlib import pyplot as plt


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('blackmagician.jpg', 0)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
print(hist.shape)
plt.hist(img.ravel(), 256)
# matlab:RGB,opencv:BGR
plt.show()


# img=cv.imread('blackmagician.jpg')
# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
# plt.show()

# mask操作
mask = np.zeros(img.shape[:2], np.uint8)
mask[50:200, 50:200] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
hist = cv.calcHist([masked_img], [0], None, [256], [0, 256])
# cv_show('masked_img', masked_img)
# plt.plot(hist, 'gray')
# plt.xlim([0,255])
# plt.show()
print(mask.shape)

# 均衡化操作(自适应直方图均衡化)
equ = cv.equalizeHist(img)
plt.hist(equ.ravel(), 256)
plt.show()
