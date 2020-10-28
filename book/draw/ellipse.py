from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()


img = np.zeros((512, 512, 3), np.uint8)
# 椭圆圆心，（长轴，短轴），起始绕逆时针旋转方向，绕顺时针起始角度与结束角度
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv_show('img', img)
