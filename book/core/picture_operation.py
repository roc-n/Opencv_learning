from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('tree.jpg')

print(img.shape)

# 拼接图像
cloud = img[280:340, 330:390]
img[273:333, 100:160] = cloud
cv_show('img', img)

# 拆分及合并
b, g, r = cv.split(img)  # 比较耗时
img = cv.merge([b, g, r])
cv_show('name', img)

b = img[:,:, 0]
g = img[:,:, 1]
r = img[:,:, 2]
img = cv.merge([b,g,r])
cv_show('name', img)


img[:,:, 0] = 0  #numpy索引进行赋值




