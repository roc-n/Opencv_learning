from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('contour,jpg', 0)
img=ret, thresh = cv.threshold(img, 127, 255, 0)
ret,contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
print(M)