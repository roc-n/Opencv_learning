from cv2 import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('image/chess.jpg')
# 转化为灰度图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化处理
ret, binary = cv.threshold(gray, 90, 255, cv.THRESH_BINARY)
cv_show('img', binary)
# 通过腐蚀去除白色噪声
kernel = np.ones((5, 5), np.uint8)
binary = cv.erode(binary, kernel)
# 平滑处理
binary = cv.medianBlur(binary, 5, 0)
cv_show('img', binary)


# Harris检测之前转换成float32类型
gray = np.float32(binary)
# 这里中间两个参数很重要，一开始没注意到
dst = cv.cornerHarris(gray, 6, 9, 0.04)
dst = cv.dilate(dst, None)
img[dst > 0.0281 * dst.max()] = [0, 0, 255]

# 以二值图形式显示修改的地方
ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
cv_show('img', dst)
# 保存图片
cv.imwrite('Tests/28-31_2.jpg', img)


# dst = np.uint8(dst)
# ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)

# corners = cv.cornerSubPix(gray, np.float32(
#     centroids), (5, 5), (-1, -1), criteria)

# res = np.hstack((centroids, corners))
# res = np.int8(res)
# img[res[:, 1], res[:, 0]] = [255, 0, 0]
# img[res[:, 3], res[:, 2]] = [0, 255, 0]

# cv.imshow('res', img)
# if cv.waitKey(0) == 27:
#     cv.destroyAllWindows()
