from cv2 import cv2 
import numpy as np
from matplotlib import pyplot as plt


def cv_show(name, img):
    cv2.imshow(name, img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
# 加载图像
img2 = cv2.imread('blackmagician.jpg')
img1 = cv2.imread('star.jpg')
# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 57, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

# plt.subplot(121), plt.imshow(mask), plt.title('mask')
# plt.subplot(122), plt.imshow(mask_inv), plt.title('mask-inv')
# plt.xticks([])
# plt.show()


# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中不为零的值对应的像素的值,其他值为 0
# 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
cv_show('imge', img1_bg)

# 取 img2 中与 mask_inv 中不为零的值对应的像素的值,其他值为 0 。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
cv_show('imge', img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
cv_show('img',dst)
img1[0:rows, 0:cols] = dst
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


