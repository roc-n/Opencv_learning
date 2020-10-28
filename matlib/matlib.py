from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 显示灰色图
img = cv.imread('tree.jpg')
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

# *******************************
# 显示彩色图(mat:RGB,opencv:BGR)

#1.
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#2.
img2 = img[:,:,::-1]

# 显示不正确的图
plt.subplot(121), plt.imshow(img)

# 显示正确的图
plt.subplot(122),
plt.xticks([]), plt.yticks([])
plt.imshow(img2)

plt.show()
# ************************************

#还可加载和保存图片
img_ = plt.imread('star.jpg')
plt.imshow(img_)
plt.show()
