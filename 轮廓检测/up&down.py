from cv2 import cv2 as cv
import numpy as np

def cv_show(img, name):
    cv.imshow('tree', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread('tree.jpg')
up = cv.pyrDown(img)
down=cv.pyrUp(img)
cv_show(img,'down')