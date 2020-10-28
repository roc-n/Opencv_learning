from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# 显示图像函数
def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()

img = cv.imread('image/zy.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # 将bgr模式转换成hsv模式

# 获取红色阈值
lower_red = np.array([160, 100, 100])
upper_red = np.array([179, 255, 255])

# 获取掩模
mask = cv.inRange(hsv, lower_red, upper_red)
# 与操作获得结果
res = cv.bitwise_and(img, img, mask=mask)
# 转换成灰度图
gray_img = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# 因res图像除了长方形外其余皆为黑色，所以阈值可以设成较低值
ret, thresh = cv.threshold(gray_img, 10, 255, cv.THRESH_BINARY)

# 进行旋转操作
rows, cols = thresh.shape[:2]
# 负号顺时针旋转，获得变换矩阵
M = cv.getRotationMatrix2D((cols / 2, rows / 2), -19.5, 1)
dst = cv.warpAffine(thresh, M, (cols, rows))


cv_show('res', res)  # 只留下长方形
cv_show('thresh', thresh)  # 二值化后的图像
cv_show('dst', dst)  # 旋转后图像
