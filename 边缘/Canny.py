from cv2 import cv2 as cv
import numpy as np
# 1.使用高斯滤波器,平滑图像,消除噪声
# 2.计算图像中每个像素点的梯度与方向（Sabel算法）
# 3.应用非极大值抑制,消除边缘检测带来的杂散影响
# 4.双阙值检测来确定真实和潜在的边缘
# 5.抑制孤立的弱边缘最终完成边缘检测

def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


        
img = cv.imread('timg.jpg', cv.IMREAD_GRAYSCALE)
v1 = cv.Canny(img, 80, 150)
v2 = cv.Canny(img, 50, 100)
res = np.hstack((v1, v2))
cv_show('res', res)
