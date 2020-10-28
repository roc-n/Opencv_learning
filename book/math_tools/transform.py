from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt


# 图像缩放与扩大，主要运用resize函数
img = cv2.imread('blackmagician.jpg')
# 下面的 None 本应该是输出图像的尺寸,但是因为后边我们设置了缩放因子
# 因此这里为 None
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# OR
# 这里呢,我们直接设置输出图像的尺寸,所以不用设置缩放因子
height, width = img.shape[:2]
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
while(1):
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()


# 平移(warpAffine函数)
img = cv2.imread('tree.jpg')
# translation = np.float32([[1, 0, 20], [0, 1, 50]])
# dst=cv2.warpAffine()


# 旋转
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -35, 1)
dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
while (1):
    cv2.imshow('img', dst)
    if cv2.waitKey(0):
        break
    cv2.destroyAllWindows()

# 仿射变换
img = cv2.imread('image/transform.jpg')
rows, cols, ch = img.shape

pst1 = np.float32([[50, 50], [200, 50], [50, 200]])
pst2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pst1, pst2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121, plt.imshow(img), plt.title('Input'))
plt.subplot(122, plt.imshow(img), plt.title('Outplot'))
plt.show()


# 透视变换
