from cv2 import cv2 as cv
import numpy as np


def cv_show(name, img):
    cv.imshow(name, img)
    k = cv.waitKey(0)
    cv.destroyAllWindows()
    if k == 27:
        cv.destroyAllWindows()


img = cv.imread('timg.jpg')
kernel = np.ones((3, 3), np.uint8)
# morphology形态学
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)


cv_show('open', opening)
cv_show('close',close)