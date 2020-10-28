from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


# 图像加法
x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x, y))  # 饱和运算,结果相对更好
print(x + y)  # 模运算

# 图像混合
img1 = cv.imread('blackmagician.jpg')
img2 = cv.imread('trees.jpg')
img2 = img2[0:300, 300:600]
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
plt.subplot(131), plt.imshow(img1, 'gray'), plt.title('magician')
plt.subplot(132), plt.imshow(img2, 'gray'), plt.title('tree')
plt.subplot(133), plt.imshow(dst, 'gray'), plt.title('fuse')
plt.show()
