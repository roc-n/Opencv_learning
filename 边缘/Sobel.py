# Sobel算子

from cv2 import cv2 as cv
import numpy as np

def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('timg.jpg', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobely = cv.convertScaleAbs(sobely)
cv_show('sobelx', sobelx)
cv_show('sobely', sobely)

sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv_show('last', sobelxy)
